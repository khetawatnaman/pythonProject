import bs4 as bs
import numpy as np
import urllib.request
import requests
from nltk import word_tokenize
from collections import Counter
domain=input("Enter the url : ")
url = "https://www." + domain
tokens=[]
st =[]
urls={}
url_count=0
urls[url]=url_count
url_count+=1
url_list=[]
local=[]
#sauce=urllib.request.urlopen(url).read()
try:
    sauce = urllib.request.urlopen(url).read()
    soup=bs.BeautifulSoup(sauce,'lxml')
    st = soup.find_all('a', href = True)
    for para in soup.find_all('p'):
        l= para.text
        tokens += word_tokenize(l)
except urllib.error.URLError as e:
    print("Error")
finally:
    pass
a=Counter(tokens)
final_tokens={}
invertedindex=[]
for i in tokens:
    if i not in final_tokens.keys():
        final_tokens[i]=len(final_tokens.keys())
        ii={}
        invertedindex.append(ii)
visited_list = []
token=[]
for i in tokens:
    if i not in token:
        token.append(i)
for i in token:
    j=final_tokens.get(i)
    k=invertedindex[j]
    k[len(visited_list)+1] = a.get(i)
    invertedindex[j] = k
frontier_list = []
for link in st:
    s=link.get('href')
    if s.startswith('http'):
        if s not in frontier_list:
            frontier_list.append(s)
            if s not in urls.keys():
                urls[s]=url_count
                url_count+=1
        if urls.get(s) is not None:
            if urls.get(s) not in local:
                local.append(urls.get(s))
url_list.append(local)

visited_list.append(url)
while frontier_list:
    url1 = frontier_list[0]
    frontier_list=frontier_list[1:]
    for a in visited_list:
        if a in url1:
            break
        else:
            tokens=[]
            st = []
            print (url1)
            '''print (len(frontier_list))
            print (len(visited_list))'''
            visited_list.append(frontier_list[0])
            try:
                sauce1=urllib.request.urlopen(url1).read()
                soup=bs.BeautifulSoup(sauce1,'lxml')
                st = soup.find_all('a', href=True);
                for para in soup.find_all('p'):
                    l= para.text
                    tokens += word_tokenize(l)
            except urllib.error.URLError:
                pass
            a=Counter(tokens)
            for i in tokens:
                if i not in final_tokens.keys():
                    final_tokens[i]=len(final_tokens.keys())
                    ii={}
                    invertedindex.append(ii)
            token=[]
            for i in tokens:
                if i not in token:
                    token.append(i)
            for i in token:
                j=final_tokens.get(i)
                k=invertedindex[j]
                k[len(visited_list)]=a.get(i)
                invertedindex[j]=k
            local=[]
            for link in st:
                s=link.get('href')
                if s.startswith('http') and "www" in s and domain not in s:
                    if s not in frontier_list and s not in visited_list:
                        frontier_list.append(s)
                        if s not in urls.keys():
                            if len(urls.keys())<200:
                                urls[s]=url_count
                                url_count += 1
                    if urls.get(s) is not None:
                        if urls.get(s) not in local:
                            local.append(urls.get(s))
            url_list.append(local)
        break 
    if len(visited_list) > 198:
       break

f = open("url_list","w")
f.write(str(urls))

print(url_list)

matrix_url = []
local=[]
len(url_list)
for i in url_list:
    for j in range(200):
        if j in i:
            local.append(1)
        else:
            local.append(0)
    matrix_url.append(local)

for i in matrix_url:
    print(i)
#print(final_tokens)
'''f=open("inverted.txt","w")
j=0
l=[]
for i in final_tokens.keys():
    l.append(i)
for i in invertedindex:
    f.write(l[j])
    f.write(" :  ")
    f.write(str(i))
    f.write("\n")
    j+=1
f.close()
termdocumentmatrix=[]
f=open("termdocumentmatrix.txt","w")
j=0'''
'''for i in invertedindex:
    n={}
    o=[]
    p=[]
    n=invertedindex[j]
    for k in n.keys():
        if k not in o:
            o.append(k)
    f.write(l[j])
    f.write(" :  ")
    for m in range(0,len(visited_list)):
        if m+1 in o:
            f.write(str(i.get(m+1)))
            p.append(i.get(m+1))
            f.write(" ")
        else:
            f.write("0")
            p.append(0)
            f.write(" ")
    f.write("\n")
    termdocumentmatrix.append(p)
    j+=1
f.close()'''
#print(invertedindex)
#print(termdocumentmatrix)
'''x=np.array(termdocumentmatrix)
np.savetxt("svd.txt", x, delimiter=" ")
y = np.loadtxt("svd.txt",delimiter=" ")
print(y)
u,s,v=np.linalg.svd(y,full_matrices=False)
np.savetxt("u.txt", u, delimiter=" ")
np.savetxt("s.txt", s, delimiter=" ")
np.savetxt("v.txt", v, delimiter=" ")'''