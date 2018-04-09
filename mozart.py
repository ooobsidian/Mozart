import codecs
import os
from bs4 import BeautifulSoup
import requests

cookies={'imslp_wiki_session':'1ff1ea59138a000fdac27acd0d3d30cf',
         'imslp_wikiLanguageSelectorLanguage':'zh',
         'imslp_wikiLoggedOut':'20180312043306',
         'imslp_wikiUserID':'191309',
         'imslp_wikiUserName':'Felixlhld',
         'imslpdisclaimeraccepted':'yes'}


base = 'http://cn.imslp.org'
header = {'Accept-Language': 'zh-CN,zh;q=0.9','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
site = 'http://cn.imslp.org/index.php?title=Category:Mozart,_Wolfgang_Amadeus&pagefrom=Fantasie+in+f+minor%2C+k.anh.0032~~mozart%2C+wolfgang+amadeus%0AFantasie+in+F+minor%2C+K.Anh.32+%28Mozart%2C+Wolfgang+Amadeus%29#mw-pages'
r = requests.get(site, headers=header,timeout=10000)
soup = BeautifulSoup(r.content, 'html.parser')
aes = soup.select('#catcolp1-1')[0].select('a')
i=1
for a in aes:
    print(i)
    url = base + a.get('href')
    u = requests.get(url, headers=header)
    Soup = BeautifulSoup(u.content, 'html.parser')
    title = Soup.select('#firstHeading')[0].text.strip().replace('/', '')
    Text = Soup.select('.wi_body')[0].text.replace('\n\n', '\t').replace('\t\n','\n').strip().replace('\n','\r\n')
    path = 'C:\\Users\\李瑞轩\\Desktop\\莫扎特1\\' + title
    try:
        os.mkdir(path)
    except:
        pass
    with codecs.open(path + '\\' + title + '.txt', "w", encoding='utf-8') as f:
       try:
           f.write(Text)
       except:
           print(title+".txt存在！")
           pass
    try:
        pdfurl = Soup.select('div[class="we_file_first we_fileblock_1"] a[class="external text"]')[0].get('href')
        with open(path + '\\' + title + '.pdf','wb') as file:
            file.write(requests.get(pdfurl,cookies=cookies,timeout=10000).content)
            print(title+"曲谱爬取完成！")
    except:
        print("曲谱不存在！")
        pass
    i=i+1
# print(soup.select('.wi_body')[0].text.replace('\n\n', '\n'))
