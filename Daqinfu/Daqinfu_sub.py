import requests
import os
import json
import random
import urllib
import time
import re
from datetime import datetime
from dateutil import tz
osenviron={}


urllist=[]
hdlist=[]


result=''


def Av(i,hd,k):
    print(str(k))
    try:
       i=i.replace(re.findall('http://(.*?)/',i)[0],'js2.a.yximgs.com')
       response = requests.get(i,headers=hd)
    except Exception as e:
      print(str(e))

def watch(flag,list):
   vip=''
   global djj_bark_cookie
   global djj_sever_jiang
   if "DJJ_BARK_COOKIE" in os.environ:
     djj_bark_cookie = os.environ["DJJ_BARK_COOKIE"]
   if "DJJ_SEVER_JIANG" in os.environ:
      djj_sever_jiang = os.environ["DJJ_SEVER_JIANG"]
   if flag in osenviron:
      vip = osenviron[flag]
   if flag in os.environ:
      vip = os.environ[flag]
   if vip:
       for line in vip.split('\n'):
         if not line:
            continue 
         list.append(line.strip())
       return list
   else:
       print(f'''【{flag}】 is empty,DTask is over.''')
       #exit()
       

def pushmsg(title,txt,bflag=1,wflag=1):
   txt=urllib.parse.quote(txt)
   title=urllib.parse.quote(title)
   if bflag==1 and djj_bark_cookie.strip():
      print("\n【通知汇总】")
      purl = f'''https://api.day.app/{djj_bark_cookie}/{title}/{txt}'''
      response = requests.post(purl)
      #print(response.text)
   if wflag==1 and djj_sever_jiang.strip():
      print("\n【微信消息】")
      purl = f'''http://sc.ftqq.com/{djj_sever_jiang}.send'''
      headers={
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
    }
      body=f'''text={txt})&desp={title}'''
      response = requests.post(purl,headers=headers,data=body)
   global result
   #print(result)
   result =''
    
def loger(m):
   print(m)
   global result
   result +=m+'\n'
    


def start():
   global urllist,hdlist,bdlist
   time.sleep(random.randint(1,5))
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   
   watch('KS_0url0',urllist)
   #watch('KS_0url1',urllist)
   #watch('KS_0url2',urllist)
   watch('KS_0headers_sub',hdlist)
   
   if(len(urllist)==0):
     print('over...........')
     exit()
   hd=eval(hdlist[0])
   T=int(datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%H", ))
   #if(T<12):
   if(len(urllist)<100):
     exit()
   for k in range(0,100):
      Av(urllist[k],hd,k+1)
      time.sleep(random.randint(3,15))
       
   
   print('🔔'*15)
   
   

if __name__ == '__main__':
       start()
    
