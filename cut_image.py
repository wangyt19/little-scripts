
import pandas as pd
import numpy as np
from xml.dom import minidom
import os
import shutil
from keras.preprocessing.image import list_pictures,array_to_img,img_to_array,load_img

def main():
image_path='A'
save_path='B'
for x in os.listdir(image_path):#注意此时A或者B下面还是有文件夹的
for y in os.listdir(os.path.join(image_path,x)):
img_path=os.path.join(image_path,x,y)
img=img_to_array(load_img(img_path))
       	       try:
                	img2=img[0:80,0:90]
except:
 	print('error:%s',%(y))
continue
filename=os.path.join(save_path,x,y)
print(y)
print(x)
print(img2.shape)
array_to_img(img2).save(filename)

if __name__=='__main__':
main()
