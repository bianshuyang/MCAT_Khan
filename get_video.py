import urllib.request
import urllib
#创建函数
def callbackfunc(blocknum, blocksize, totalsize):
    percent = int(100.0 * blocknum * blocksize / totalsize)
    if percent > 100:
        percent = 100
    if (percent/10)==int(percent/10):
        print ('下载了这个视频的',percent,'%')
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
def get_title(line):
    start = '/v/'
    return(line[line.index(start)+3:])
    print ('getting title...')
    print (line[line.index(start)+3:])
def get_htitle(line):
    start = '/a/'
    return(line[line.index(start)+3:])
    print ('getting title...')
    print (line[line.index(start)+3:])
def get_video(link,title): 
    urllib.request.urlretrieve(link,title,callbackfunc)
def get_teach_link(category_link):
    url = category_link##'https://www.khanacademy.org/test-prep/mcat/cells#cell-membrane-overview'
    res = urllib.request.urlopen(url=url)
    page_source = res.read().decode('utf-8')
    with open('a.txt','w',encoding = 'utf-8') as f:
        f.write(page_source)
    print ("all links written to the designated desk")
def break_down_link(urltext):
    try:
        with open(urltext,'r',encoding='utf-8',errors='ignore') as f:
            a =f.readlines()
        a = ''.join(a)
        key = 1
        q = 'about'
        while (q=='') is False:
            start = 'nodeUrl'
            end = 'description'
            with open(location+'\\'+str(key)+'.txt','w') as f:
                    a = a.replace(a[0:a.index(start)-10],'')
                    q = (a[a.index(start):a.index(end)])
                    f.write(q)
            a = a.replace(q,'')
            key = key+1
    except:
        print ('end of page')

def create_folders():
    import os
    a = os.listdir(os.getcwd())
    a.remove('link.txt')
    a.remove('a.txt')
    a.remove('get_video.py')
    video = []
    exercise = []
    article = []
    for i in a:
        try:
            with open(i,'r') as f:
                link = f.readlines()
                link = ''.join(link)
            link = link.replace('nodeUrl\": \"','')
            if 'Article' in link:
                link = link.replace('nodeUrl','')
                end = 'kind'
                link = link[0:link.index(end)]
                link = link.replace("\\","")
                link = link.replace('"','')
                link = link.replace(':','')
                link = link.replace(' ','')
                link = link.replace(',','')
                article.append(link)
            else:
                if 'Exercise' in link:
                    link = link.replace('nodeUrl','')
                    end = 'isSkillCheck'
                    link = link[0:link.index(end)]
                    link = link.replace("\\","")
                    link = link.replace('"','')
                    link = link.replace(':','')
                    link = link.replace(' ','')
                    link = link.replace(',','')
                    exercise.append(link)
                else:
                    link = link.replace('nodeUrl','')
                    end = 'kind'
                    link = link[0:link.index(end)]
                    link = link.replace("\\","")
                    link = link.replace('"','')
                    link = link.replace(':','')
                    link = link.replace(' ','')
                    link = link.replace(',','')
                    video.append(link)
        except:
            print ('reach an empty file')
    print('all links obtained success')
    for i in a:
        os.remove(i)
    os.remove('link.txt')
    os.remove('a.txt')
    videos = []
    for i in video:
        videos.append('https://www.khanacademy.org'+i)
    exercises = []
    for i in exercise:
        exercises.append('https://www.khanacademy.org'+i)
    articles = []
    for i in article:
        articles.append('https://www.khanacademy.org'+i)
    os.makedirs(os.getcwd()+'\\videos')
    with open(os.getcwd()+'\\videos\\'+'videos.txt','w') as f:
        f.write('\n'.join(videos))
    os.makedirs(os.getcwd()+'\\exercises')
    with open(os.getcwd()+'\\exercises\\'+'exercises.txt','w') as f:
        f.write('\n'.join(exercises))
    os.makedirs(os.getcwd()+'\\articles')
    with open(os.getcwd()+'\\articles\\'+'articles.txt','w') as f:
        f.write('\n'.join(articles))
    print ('creating folders success')
with open('link.txt','r') as f:
    a = f.readlines()
a = ''.join(a)
a = a.replace('\n','')
get_teach_link(a)
break_down_link('a.txt')
create_folders()
import os
import shutil
with open(os.getcwd()+'\\'+'videos'+'\\'+'videos.txt') as f:
    a = f.readlines()
link = []
for i in a:
    i = i.replace('\n','')
    link.append(i)
##
a = os.getcwd()
a = a.replace('D:\Khan_MCAT','')
a = a.replace('videos','')
a = a.replace('\\','/')
links = []
for i in link:
    if a in i:
        links.append(i)
    else:
        xm = 0
for i in links:
    get_video(str(get_video_link(i)),str(get_title(i))+'.mp4')
    shutil.move(os.getcwd()+'\\'+str(get_title(i))+'.mp4',os.getcwd()+'\\'+'videos'+'\\'+str(link.index(i))+'-'+str(get_title(i))+'.mp4')
    os.remove('1.txt')
with open(os.getcwd()+'\\'+'articles'+'\\'+'articles.txt') as f:
    a = f.readlines()
link = []
for i in a:
    i = i.replace('\n','')
    link.append(i)
##def getHtml(url):
##    html = urllib.request.urlopen(url).read()
##    return html
##def saveHtml(file_name,file_content):  
##    with open (os.getcwd()+'\\'+'articles'+'\\'+file_name,"wb") as f:
##        f.write(file_content)  
##for i in link:
##    html = getHtml(i)
##    print (i)
##    saveHtml(get_htitle(i),html)
##    print(get_htitle(i))
