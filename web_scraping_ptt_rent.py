from bs4 import BeautifulSoup
import requests
import csv
import re 
url="https://www.ptt.cc/bbs/Rent_apart/index6.html"

ptt_title=[]
ptt_author=[]
ptt_time=[]
ptt_url=[]
ptt_phone=[]
ptt_rent=[]
ptt_footage=[]
ptt_ip=[]
ptt_address = []
ptt_gender = []
a=0
#%%

def get_article_content(article_url):
    r = requests.get(article_url)
    r.encoding='utf-8'
    soup = BeautifulSoup(r.text, "lxml")
    results = soup.select('span.article-meta-value')
    content=soup.select('#main-content')[0].get_text()
    phone_fliter=re.compile('09\d{1,2}\-?\d{3}\-?\d{3}')
    ip_fliter=re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    rent_filter = re.compile('租金：.{1,10}')
    footage_filter = re.compile('\(?\d{2}\)?[.]\d{2}\坪')
    footage_filter2 = re.compile('\d{2}\坪')
    address_filter = re.compile('地址：.{1,30}')
    #for 徵
    address_filter2 = re.compile('地區：.{1,30}')
    rent_filter2 = re.compile('月租：.{1,15}')
    gender_filter = re.compile('性別：.{1,3}')
    if len(results)==4:
        ptt_url.append(article_url)
        ptt_author.append(results[0].text)
        ptt_title.append(results[2].text)
        ptt_time.append(results[3].text)
        if content and ('徵' in results[2].text) == True:            
            ptt_phone.append(phone_fliter.findall(content))
            ptt_footage.append('')
            rent = rent_filter2.findall(content)
            ptt_rent.append(rent)
            address = address_filter2.findall(content)
            ptt_address.append(address)
            gender = gender_filter.findall(content)
            ptt_gender.append(gender)
            if len(ip_fliter.findall(content)) != 0 :
                ptt_ip.append(ip_fliter.findall(content)[0])
            else:
                ptt_ip.append('')
        if content and ('徵' in results[2].text) == False:
            ptt_phone.append(phone_fliter.findall(content))
            footage = footage_filter.findall(content)
            if footage == []:
                footage = footage_filter2.findall(content)
            ptt_footage.append(footage)
            rent = rent_filter.findall(content)
            ptt_rent.append(rent)
            address = address_filter.findall(content)
            ptt_address.append(address)
            ptt_gender.append('')
            if len(ip_fliter.findall(content)) != 0 :
                ptt_ip.append(ip_fliter.findall(content)[0])
            else:
                ptt_ip.append('')
                

def get_all_href(url):
    r = requests.get(url)
    r.encoding='utf-8'
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.select("div.title")
    for item in results:
        a_item = item.select_one("a")
        if a_item:
            get_article_content(article_url='https://www.ptt.cc'+a_item.get('href'))
for page in range(1,237):
    r = requests.get(url)
    r.encoding='utf-8'
    soup = BeautifulSoup(r.text,"html.parser")
    btn = soup.select('div.btn-group > a')
    up_page_href = btn[3]['href']
    next_page_url = 'https://www.ptt.cc' + up_page_href
    url = next_page_url
    get_all_href(url = url)
    a=a+1
    print('page %d done'%a)
#%%
while '' in ptt_footage:
    ptt_footage.remove('')
#ptt_footage.remove('')
#%%
with open(r'C:\Users\U360\Desktop\ptt_list_0418_12.csv', 'w',encoding = 'utf_8_sig') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    newrow = ['title', 'author', 'time', 'url','phone','address','rent','footage','gender','ip']
    csvwriter.writerow(newrow)
    for n in range(0, len(ptt_title)):
        newrow.clear()
        newrow.append(ptt_title[n])
        newrow.append(ptt_author[n])
        newrow.append(ptt_time[n])
        newrow.append(ptt_url[n])
        newrow.append(ptt_phone[n])
        newrow.append(ptt_address[n])
        newrow.append(ptt_rent[n])
        newrow.append(ptt_footage[n])
        newrow.append(ptt_gender[n])
        newrow.append(ptt_ip[n])
        csvwriter.writerow(newrow)
#%%
