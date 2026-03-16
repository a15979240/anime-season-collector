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

# 偽裝瀏覽器
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
# 轉碼
da=response.read().decode("utf-8")
# 讀取一行
# da=response.readline()
# 資料清洗取繁中名稱
re_d=re.compile(r'<div class="anime_info anime_names site-content-float"><h3 class="entity_localized_name">(.*?)</h3><div class="notranslate entity_original_name">')
fin_ANI_name_CT0=re_d.findall(da)#中
# 資料清洗取日文名稱
reo=re.compile(r'</div><div class="notranslate entity_original_name">(.*?)</div></div><div class="anime_specs"><div class="anime_tag">')
fin_ANI_name_JP0=reo.findall(da)#日
# print(fin_ANI_name_CT)


# 重整
# 繁中
fin_ANI_name_CT=[]
for i in range(len(fin_ANI_name_CT0)):
    if '</h3><div class="entity_alternative_name">' in fin_ANI_name_CT0[i]:
        finCT_t1=str(fin_ANI_name_CT0[i]).split('</h3><div class="entity_alternative_name">')
        finCT_t1=finCT_t1[0]
        fin_ANI_name_CT.append(finCT_t1)
        finCT_t2=str(fin_ANI_name_CT0[i]).split('<h3 class="entity_localized_name">')
        finCT_t2=finCT_t2[-1]
        fin_ANI_name_CT.append(finCT_t2)
    else:
        fin_ANI_name_CT.append(fin_ANI_name_CT0[i])
# 日文
fin_ANI_name_JP=[]
for i in range(len(fin_ANI_name_JP0)):
    if '</div></div><div class="anime_info main site-content-float">' in fin_ANI_name_JP0[i]:
        fo_t1=str(fin_ANI_name_JP0[i]).split('</div></div><div class="anime_info main site-content-float">')
        fo_t1=fo_t1[0]
        fin_ANI_name_JP.append(fo_t1)
        
    else:
        fin_ANI_name_JP.append(fin_ANI_name_JP0[i])



# 日文名稱轉羅馬拼音
foJE=[]
for i in range(len(fin_ANI_name_JP)):
    foe=conv.do(fin_ANI_name_JP[i])
    foJE.insert(i,foe)
print(foJE)

print(fin_ANI_name_CT)
# </h3><div class="entity_alternative_name">
# 組合中日羅
finCTJE=[]
# finCT1=''
for j in range(len(fin_ANI_name_CT)):
    # finCT1=str(fin_ANI_name_CT[j]).split('</h3><div class="entity_alternative_name">')
    # finCT1=finCT1[0]
    f=fin_ANI_name_CT[j]+"_"+fin_ANI_name_JP[j]+"_"+foJE[j]#中日羅
    finCTJE.insert(j,f)
print(type(finCTJE))#屬性檢查

z="\n".join(fin_ANI_name_JP)
Flist=finCTJE
# 建立TXT清單
SEC=str(input("是否建立整合TXT檔(Y/N):"))

if SEC == "Y":
    FCTJE=open(r'E:\\VCB-ANIME\\已上傳\\'+x+'.txt',"wb")
    FCTJE.write("\n".join(finCTJE).encode())#lis轉字串並寫入
    FCTJE.write("".join("\nend").encode())#lis轉字串並寫入
    FCTJE.close()
    print("執行結束")
else:
    print("執行結束")

# print(foJE[-2])
# z0=conv.do(z)
# 建立CSV檔或EXCEL
# 中日羅整合，next gui列表