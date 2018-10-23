import os
dir_img='imgtest'
dir_label=dir_img+'_label'
def makedirs_quietly(d):
  if not os.path.exists(d):
    os.makedirs(d)
makedirs_quietly(dir_label)
for x in os.listdir(dir_image):
  txt_path=os.path.join(dir_label,x.split('.')[0]+'.txt')
  with open(txt_path,'w') as f:
    f.write('0')
