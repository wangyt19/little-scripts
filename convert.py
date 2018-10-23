from model import ctc_model_4pd
import os
import tensorflow as tf
from keras import backend as K
from keras.models import Model
import logging
from tensorflow.python.util import compat
import argparse
import sys

os.environ["CUDA_VISIBLE_DEVICES"] = ''
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
K.set_session(tf.Session(config=config))
K.set_learning_phase(0)

def export_savedmodel(model, model_path='model'):
    logging.info("Model input: {}, output: {}".format(model.input, model.output))
    model_signature = tf.saved_model.signature_def_utils.predict_signature_def(
            inputs={'input': model.input}, outputs={'output': model.output})

    model_version = 1
    export_path = os.path.join(
            compat.as_bytes(model_path), compat.as_bytes(str(model_version)))
    logging.info("Export the model to {}".format(export_path))

    builder = tf.saved_model.builder.SavedModelBuilder(export_path)
    builder.add_meta_graph_and_variables(
            sess=K.get_session(),
            tags=[tf.saved_model.tag_constants.SERVING],
            clear_devices=True,
            signature_def_map={
                tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
                    model_signature
            })
    builder.save()


def parse_args():
  parser = argparse.ArgumentParser(description='Convert a recog trained model')
  parser.add_argument('--model_type', dest='model_type', help='model type lower/upper', type=str)
  parser.add_argument('--model_architecture', dest='model_architecture', help='model architecture', type=str)
  parser.add_argument('--keras_model_path', dest='keras_model_path', help='keras model path', type=str)
  parser.add_argument('--tf_coverted_model_path', dest='tf_coverted_model_path', 
    help='tf converted model path', type=str)
  if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

  args = parser.parse_args()
  return args

def main():
    args = parse_args()
    #hyperparameters
    #48 for lowercase, 70 for uppercase
    if args.model_type == 'lower':
        target_height = 48
        n_class = 11
    elif args.model_type == 'upper':
        target_height = 70
        n_class = 20
    else:
        raise Exception('error')

    rnn_size = 128

    model_architecture = args.model_architecture
    keras_trained_model_path = args.keras_model_path
    model_path = args.tf_coverted_model_path

    ctc_model = ctc_model_4pd(target_height, rnn_size, n_class, model_architecture)
    ctc_model.model.load_weights(keras_trained_model_path)

    model = ctc_model.model
    export_savedmodel(model, model_path)

if __name__ == '__main__':
    main()
