import urllib.request
import urllib
import time
def callbackfunc(blocknum, blocksize, totalsize):
    percent = int(100.0 * blocknum * blocksize / totalsize)
    if percent > 100:
        percent = 100
    if (percent/10)==int(percent/10):
        print ('下载了这个视频的',percent,'%')
        percent = percent+1
    else:
        xiaoming = 0
def get_video_link(teach_link): #'https://www.khanacademy.org/test-prep/mcat/cells/cell-membrane-overview/v/cell-membrane-introduction'
    url = teach_link
    res = urllib.request.urlopen(url=url)
    page_source = res.read().decode('utf-8')
    with open('1.txt','w',encoding = 'utf-8',errors='ignore') as f:
        f.write(page_source)
    with open('1.txt','r',encoding='utf-8',errors='ignore') as f:
        a = f.readlines()
    a = ''.join(a)
    head = 'https://cdn.kastatic.org/ka-youtube-'
    end = '","png":"https://cdn.kastatic'
    link = a[a.index(head):a.index(end)]
    return (link)
    print ('getting_link...',link)
def get_video_link_otherwise(teach_link): #'https://www.khanacademy.org/test-prep/mcat/cells/cell-membrane-overview/v/cell-membrane-introduction'
    url = teach_link
    res = urllib.request.urlopen(url=url)
    page_source = res.read().decode('utf-8')
    with open('1.txt','w',encoding = 'utf-8',errors='ignore') as f:
        f.write(page_source)
    with open('1.txt','r',encoding='utf-8',errors='ignore') as f:
        a = f.readlines()
    a = ''.join(a)
    head = 'low.mp4","mp4":"https://cdn.kastatic.org'
    end = '.mp4","m3u8":'
    link = a[a.index(head):a.index(end)+len(end)]
    link = link.replace('","m3u8":','')
    link = link.replace('low.mp4","mp4":"','')
    return (link)
    print ('getting_link...',link)
def get_title(line):
    start = '/v/'
    return(line[line.index(start)+3:])
    print ('getting title...')
    print (line[line.index(start)+3:])
def get_video(link,title): 
    urllib.request.urlretrieve(link,title,callbackfunc)
import os
import shutil
with open(os.getcwd()+'\\'+'videos'+'\\'+'videos.txt') as f:
    a = f.readlines()
link = []
for i in a:
    i = i.replace('\n','')
    link.append(i)
##
upupfolder = os.path.abspath(os.path.join(os.getcwd(), "../.."))
a = os.getcwd()
a = a.replace(upupfolder+'\\','')
a = a.replace('videos','')
a = a.replace('\\','/')
links = []
for i in link:
    if a in i:
        links.append(i)
    else:
        xm = 0
links = list(set(links))
saved = os.listdir(os.getcwd()+'\\'+'videos')
used = []
for i in links:
    for j in saved:
        if get_title(i) in j:
            used.append(i)
reallink = []
for i in links:
    if i in used:
        print(get_title(i),'used')
    else:
        reallink.append(i)
for i in reallink:
    print(get_title(i),'now downloading...')
    try:
        get_video(str(get_video_link(i)),str(get_title(i))+'.mp4')
    except:
        get_video(str(get_video_link_otherwise(i)),str(get_title(i))+'.mp4')
        #get_video_link_otherwise
    shutil.move(os.getcwd()+'\\'+str(get_title(i))+'.mp4',os.getcwd()+'\\'+'videos'+'\\'+str(link.index(i))+'-'+str(get_title(i))+'.mp4')
    os.remove('1.txt')
