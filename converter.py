####frame
import os
##def break_links_into_folder(file):
##    with open(file,'r') as f:
##        a = f.readlines()
##    grand_folder = []
##    small_folder = []
##    for i in a:
##        i = i.replace('{"url":"/test-prep/mcat/','')
##        i = i.replace('#','\\')
##        i = i.replace('\n','')
##        os.makedirs(os.getcwd()+'\\'+i)
##break_links_into_folder('links.txt')
######
######break_links_into_folder('links.txt')
pre = 'https://www.khanacademy.org/test-prep/mcat/'
files= os.listdir('D:\\Khan_MCAT')
files.remove('converter.py')
files.remove('get_video.py')
files.remove('behavior')
files.remove('biological-sciences-practice')
files.remove('biomolecules')
import shutil
for g in files:
    q = os.listdir('D:\\Khan_MCAT'+'\\'+g)
    for i in q:
        second_link = ('https://www.khanacademy.org/test-prep/mcat/'+g+'#'+i)
     #   with open('D:\Khan_MCAT'+'\\'+g+'\\'+i+'\\'+'link.txt','w') as f:
 #           f.write(second_link)
 #           shutil.copy('D:\\Khan_MCAT\\get_video.py','D:\Khan_MCAT'+'\\'+g+'\\'+i+'\\'+'get_video.py')
        loc = 'D:\Khan_MCAT'+'\\'+g+'\\'+i
        print ('cd '+  loc+' & python '+loc+'\\'+'get_video.py')
##        os.remove('D:\Khan_MCAT'+'\\'+g+'\\'+i+'\\'+'link.txt')
##        os.remove('D:\Khan_MCAT'+'\\'+g+'\\'+i+'\\'+'get_video.py')
#####write_in_each_folder()
####cut_link_into_sub_folders()
####convert_videos_in_video_folder()
####convert_articles_in_article_folder()
