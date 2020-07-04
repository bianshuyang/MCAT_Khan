import os
files= os.listdir(os.getcwd())
files.remove('create_folders.py')
files.remove('get_folder.bat')
files.remove('get_videos.py')
files.remove('main.py')
files.remove('submain.py')
content = []
course_type = 'nclex-rn'
import shutil
for g in files:
    q = os.listdir(os.getcwd()+'\\'+g)
    for i in q:
        shutil.copy(os.getcwd()+'\\get_videos.py',os.getcwd()+'\\'+g+'\\'+i+'\\'+'get_videos.py')
        content.append('cd '+os.getcwd()+'\\'+g+'\\'+i+'\n'+'python get_videos.py')
with open('get_video.bat','w') as f:
    f.write('\n'.join(content))
print('your next step is to run this bat file')

