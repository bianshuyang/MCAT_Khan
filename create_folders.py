import urllib.request
import urllib
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
            with open(str(key)+'.txt','w') as f:
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
    a.remove('create_folders.py')
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
