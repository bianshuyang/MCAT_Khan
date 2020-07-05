import os
files= os.listdir(os.getcwd())
import shutil
content = []
for g in files:
    try:
        q = os.listdir(os.getcwd()+'\\'+g)
        for i in q:
            shutil.copy(os.getcwd()+'\\exercise_grand_pre_final.py',os.getcwd()+'\\'+g+'\\'+i+'\\'+'exercises\\'+'exercise_grand.py')
            content.append('cd '+os.getcwd()+'\\'+g+'\\'+i+'\\exercises\n'+'python exercise_grand.py')
    except:
        print(g)
        print('not folder')
with open('get_exercise.bat','w') as f:
    f.write('\n'.join(content))
print('your third step is to run this bat file')
