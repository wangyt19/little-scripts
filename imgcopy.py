fileDir='A'
tarDir='B'
import os,shutil,random
def Copyfile(fileDir):
  pathDir=os.listdir(fileDir)
  sample=random.sample(pathDir,1000)
  for name in sample:
    shutil.copyfile(fileDir+name,tarDir+name)
    #shutil.move(fileDir+name,tarDir+name)
if __name__=='__main__':
  Copyfile(fileDir)
