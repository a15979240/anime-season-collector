import urllib.request
import random
import re
import pykakasi
from pykakasi import kakasi

kakasi = kakasi()
kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')
conv = kakasi.getConverter()

# 偽裝瀏覽器#
x=str(input("輸入動畫季度:"))
url="https://acgsecrets.hk/bangumi/"+x+"/"
# 模擬請求頭
# 完整請求頭
headers={
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"
}
# 設置一個請求器
req=urllib.request.Request(url,headers=headers)
# 發起請求
response=urllib.request.urlopen(req)
da=response.read().decode("utf-8")
# 讀取一行
# da=response.readline()
re_d=re.compile(r'<div class="anime_info anime_names site-content-float"><h3 class="entity_localized_name">(.*?)</h3><div class="notranslate entity_original_name">')
reo=re.compile(r'</div><div class="notranslate entity_original_name">(.*?)</div></div><div class="anime_specs"><div class="anime_tag">')
finCT0=re_d.findall(da)#中
# print(finCT)

fo0=reo.findall(da)#日
# 重整
finCT=[]
for i in range(len(finCT0)):
    if '</h3><div class="entity_alternative_name">' in finCT0[i]:
        finCT_t1=str(finCT0[i]).split('</h3><div class="entity_alternative_name">')
        finCT_t1=finCT_t1[0]
        finCT.append(finCT_t1)
        finCT_t2=str(finCT0[i]).split('<h3 class="entity_localized_name">')
        finCT_t2=finCT_t2[-1]
        finCT.append(finCT_t2)
    else:
        finCT.append(finCT0[i])
fo=[]
for i in range(len(fo0)):
    if '</div></div><div class="anime_info main site-content-float">' in fo0[i]:
        fo_t1=str(fo0[i]).split('</div></div><div class="anime_info main site-content-float">')
        fo_t1=fo_t1[0]
        fo.append(fo_t1)
        
    else:
        fo.append(fo0[i])




foJE=[]
for i in range(len(fo)):
    foe=conv.do(fo[i])
    foJE.insert(i,foe)
print(foJE)

print(finCT)
# </h3><div class="entity_alternative_name">
finCTJE=[]
finCT1=''
for j in range(len(finCT)):
    # finCT1=str(finCT[j]).split('</h3><div class="entity_alternative_name">')
    # finCT1=finCT1[0]
    f=finCT[j]+"_"+fo[j]+"_"+foJE[j]#中日羅
    finCTJE.insert(j,f)
print(type(finCTJE))

z="\n".join(fo)
Flist=finCTJE

SEC=str(input("是否建立整合TXT檔(Y/N):"))

if SEC == "Y":
    FCTJE=open(r'E:\\VCB-ANIME\\已上傳\\'+x+'.txt',"wb")
    FCTJE.write("\n".join(finCTJE).encode())#lis轉字串並寫入
    FCTJE.write("".join("\nend").encode())#lis轉字串並寫入
    FCTJE.close()
    print("執行結束")
else:
    print("執行結束")

print(foJE[-2])
z0=conv.do(z)

# 中日羅整合，next gui列表