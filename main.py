import os
import urllib.request
from urllib.request import *
course_type = input('What test-related courses do you wish: https://www.khanacademy.org/test-prep/')
link = 'https://www.khanacademy.org/test-prep/'+course_type
result = urlopen(link)
print('opened')
with open('link.txt','w',encoding = 'utf-8',errors='ignore') as f:
    data = result.read()
    print('read')
    f.write(data.decode('utf-8'))
with open('link.txt','r',encoding = 'utf-8',errors='ignore') as f:
    a = f.readlines()
grand_folder = []
small_folder = []
start = '{"url":"/test-prep/'+course_type+'/'
end = '11bfxfy","_11dj4vig","_12r4ewyx","_12yy6f6l","_13420gg"'
a = ''.join(a)
b = a[a.index(start):a.index(end)]
with open('link2.txt','w',encoding = 'utf-8',errors = 'ignore') as f:
    f.write(b)
with open('link2.txt','r',encoding = 'utf-8',errors = 'ignore') as f:
    a = f.readlines()
a = ''.join(a)
linking = []
link = 'about'
try:
    while (link=='')== False:
        start = '"url":"'
        end = '","title":"'
        link= a[a.index(start)+len(start):a.index(end)]
        linking.append(link)
        a = a.replace(a[a.index(start):a.index(end)+len(end)],'')
except:
    print('reach_end')
import os
linking = list(set(linking))
for i in linking:
    i = i.replace('/test-prep/'+course_type+'/','') ###You can change it into any other folder, such as GRE, etc.
    i = i.replace('#','\\')
    i = i.replace('\n','')
    try:
        os.makedirs(os.getcwd()+'\\'+i)
    except:
        print('already exist')
import os

try:
    os.remove('link2.txt')
    os.remove('link.txt')
except:
    print()
files= os.listdir(os.getcwd())
files.remove('main.py')
files.remove('create_folders.py')
content = []
course_type = 'nclex-rn'
import shutil
for g in files:
    q = os.listdir(os.getcwd()+'\\'+g)
    for i in q:
        shutil.copy(os.getcwd()+'\\create_folders.py',os.getcwd()+'\\'+g+'\\'+i+'\\'+'create_folders.py')
        second_link = 'https://www.khanacademy.org/test-prep/'+course_type+'/'+g+'#'+i
        with open(os.getcwd()+'\\'+g+'\\'+i+'\\'+'link.txt','w') as f:
            f.write(second_link)
        content.append('cd '+os.getcwd()+'\\'+g+'\\'+i+'\n'+'python create_folders.py')
with open('get_folder.bat','w') as f:
    f.write('\n'.join(content))
print('your next step is to run this bat file')

