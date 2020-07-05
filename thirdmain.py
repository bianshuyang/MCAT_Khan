import os
files= os.listdir(os.getcwd())
k = ['create_folders.py','get_folder.bat','get_video.bat','get_videos.py','main.py','submain.py','thirdmain.py','get_article.py']
for i in k:
    files.remove(i)
print(files)
content = []
import shutil
for g in files:
    q = os.listdir(os.getcwd()+'\\'+g)
    for i in q:
        shutil.copy(os.getcwd()+'\\get_article.py',os.getcwd()+'\\'+g+'\\'+i+'\\'+'articles\\'+'get_article.py')
        content.append('cd '+os.getcwd()+'\\'+g+'\\'+i+'\\articles\n'+'python get_article.py')
with open('get_article.bat','w') as f:
    f.write('\n'.join(content))
print('your third step is to run this bat file')

