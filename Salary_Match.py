import pandas as pd
a=pd.read_csv(r'C:\Users\U360\Desktop\四下資料\總部數據建模計畫\ptt\主計list2.csv',encoding='big5', engine = 'python')
a1=pd.read_csv(r'C:\Users\U360\Desktop\四下資料\總部數據建模計畫\ptt\ccoclist.csv',encoding='utf-8-sig', engine = 'python')
print(a1)
#%%
job=pd.read_excel(r'C:\Users\U360\Desktop\四下資料\總部數據建模計畫\ptt\job.xlsx',encoding='utf-8')

#%%
b=[]
tem=[]
for i in a.columns:
    b.append('%s'%i)
    tem.append('%s'%i)
b1=[]#ccoc
b2=[]#ccoc碼
for i in a1.columns:
    b1.append(i)
    b2.append(a1[i][0])
b3=[]#主計處結果
print(b)
#%%
fileTrainRead=tem
for i in range(len(b1)):
    fileTrainRead.append(b1[i])

#%%
import jieba
stopWords=['-','、',')','(','人',':','/','之','及','，']
#jieba.lcut返回一list,jieba.cut返回一iterator
fileTrainSeg=[]
for i in range(len(fileTrainRead)):
    fileTrainSeg.append(jieba.lcut(fileTrainRead[i],cut_all=False))
    #filter(function, iterable)
    #lambda(arg1, arg2, ....: expression)
    fileTrainSeg=list(filter(lambda q: q not in stopWords, fileTrainSeg))
#%%
jobcut=[]
stopWords=['-','、',')','(','人',':','/','之','及','，','']
for i in range(328):
    jobcut.append(jieba.lcut(job['職業分類表 \t中分類 \t小分類 \t'][i],cut_all=False))
for i in range(328):
    for j in range(len(jobcut[i])):
        #strip()移除字符串頭尾指定的字符序列，如果不带参数，默認是清除两邊的空白符，例如：/n, /r, /t, ' '
        jobcut[i][j]=jobcut[i][j].strip()
for i in range(328):
    for j in range(len(jobcut[i])):
            jobcut[i]=list(filter(lambda q: q not in stopWords, jobcut[i]))
#%%
fileTrainSeg=fileTrainSeg+jobcut
#%%
from gensim.models.word2vec import Word2Vec
model = Word2Vec(fileTrainSeg, size=250, iter=8)
#%% 
import jieba
import re
alist=[]
done=[]
df=pd.DataFrame()

stopWords=['人員','員','工人','工人員','-','、',')','(','服務業','人','業','一般',':','/','術員','事業','其他','之','如','及']
#user_input是模糊比對後的相似詞，collection是主計處的工作列表
#從match取得模糊比對單詞至主計處尋找相似工作
def fuzzyfinder(user_input, collection):
    global alist
    suggestions = []
    pattern = '.*?'.join(jieba.cut(user_input)) 
    regex = re.compile(pattern)
    for item in collection:
        match = regex.search(item)
        if match:
            suggestions.append((len(match.group()), match.start(), item))
    #use underscore(_) to seperate words
    #????suggestion是
    temp=[x for _, _, x in sorted(suggestions)]
    return temp

#把ccoc切塊並去除停用詞
def cutter(entersentence):
    global stopWords
    sentencecut=jieba.lcut(entersentence)
    sentencecut=list(filter(lambda q: q not in stopWords, sentencecut))
    return sentencecut
#切塊後模糊比對的單詞進入FUZZYFINDER尋找包含這些相似詞的工作，並取各相似詞前十名。
def fuzzymatch(matchword):
    global df
    global done
    try:
        res=list(model.wv.most_similar(matchword, topn=2))
        lis=[]
        lis.append(matchword)
        for i in res:
            lis.append(i[0])
#    df[matchword]=lis
        for j in lis: 
            get=fuzzyfinder(j,b)[0:10]
            done=done+get
            
    except: 
        return []
        
    
#%%
fuzzymatch('資訊')
#%%
targetlist=[]
donelist=[]
#b1 ==ccoc
for o in range(1041):        
    target=b1[o]
    df=pd.DataFrame()  
    done=[]
    cutres=cutter(target)#呼叫ccoc切塊功能，返還一list
    #取ccoc切塊list逐一做模糊比對
    for i in cutres:
        fuzzymatch(i)
#    if len(done)!=0:
#        targetlist.append(target)
#        donelist.append(list(set(done)))
#    print(target)
    if len(list(set(done))) ==0:
        donelist.append('none')
    else:
        donelist.append(list(set(done)))

#%%
import csv
with open(r'C:\Users\U360\Desktop\四下資料\總部數據建模計畫\ptt\matchlist.csv', 'w',) as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    newrow = ['ccoc_target','match_value']
    csvwriter.writerow(newrow)
    for n in range(0, len(donelist)):
        newrow.clear()
        newrow.append(b1[n])
        newrow.append(donelist[n])
        csvwriter.writerow(newrow)
    
#%%
target=b1[3]
df=pd.DataFrame()  
done=[]
cutres=cutter(target)
for i in cutres:
    fuzzymatch(i)
print('待比對的ccoc: ',target)    
print('比對結果: ',list(set(done)))
#%%    
    
