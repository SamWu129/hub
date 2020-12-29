import requests
import os
import json
import random
import urllib
import time
from datetime import datetime
from dateutil import tz
osenviron={}
djj_bark_cookie=''
djj_sever_jiang=''


urllist=[]
hdlist=[]
bdlist=[]
result=''
ID=''
def Av(i,hd,j,k):
    print('=🔔='*k)
    global ID
    try:
      
       response = requests.post(i,headers=eval(hd),data=j)
       Res=response.json()
       #print(Res)
       if(k==1):
           print(Res['code'])
       elif(k==2):
         print(Res['code'])
         for item in Res['data']['task_list']:
           if(json.dumps(item).find('get_coin')>0):
             
             if(item['status']==2):
               Av(urllist[2],hdlist[0],bdlist[0],3)
       elif(k==3 or k==4 or k==5):
          print(Res['code'])
       elif(k==6):
          for item in Res['data']['items']:
           if 'auth' in item.keys():
             ID=f'''【{item['auth']['auth_id']}】{item['auth']['nickname'][0:3]}'''
          Av(urllist[k]+str(item['auth']['auth_id']),hdlist[0],bdlist[0],(k+1))
       elif(k==7):
       	    loger(f'''{ID}|{Res['data']['score']}|{int(Res['data']['today_score'])/10000}''')
    except Exception as e:
      print(str(e))


def watch(flag,list):
   vip=''
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
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
       pushmsg('Youku',result)
       exit()
       

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
   #print(m)
   global result
   result +=m+'\n'
    
def notice(b,e):

    ll=False

    start_time = datetime.strptime(str(datetime.now().date())+b, '%Y-%m-%d%H:%M')

    end_time =  datetime.strptime(str(datetime.now().date())+e, '%Y-%m-%d%H:%M')

    now_time = datetime.now()

    if now_time > start_time and now_time<end_time:

       ll=True

    else:

    	ll=False

    return ll

def start():
   global bdlist,urllist,hdlist
   time.sleep(random.randint(1,5))
   watch('sam_url',urllist)
   watch('sam_headers',hdlist)
   for j in range(5):
     for j in range(7):
       print('====count===='+str(j+1))
       #if(j<2):
         #continue
       bdlist=[]
       watch('sam_body'+str(j),bdlist)
       #print(bdlist)
       if(len(bdlist)==0):
            break
       for k in range(len(urllist)):
          if(k==2 or k==6):
             continue
          Av(urllist[k],hdlist[0],bdlist[0],(k+1))
          time.sleep(random.randint(2,4))
       time.sleep(random.randint(1,4))
       print('🔔'*15)
       if notice('4:00','5:00') or notice('22:00','23:00') or notice('13:00','14:00'):
       pushmsg('Youku',result)
   

if __name__ == '__main__':
       start()
    
