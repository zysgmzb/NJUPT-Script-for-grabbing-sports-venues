from Crypto.Cipher import AES
import requests
import base64
import json
import time
import datetime


def getsig(timestamp):
    iv = b'25d82196341548ef'
    key = b'6f00cd9cade84e52'
    def pad(s): return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    ciphertext = pad(timestamp)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encryptedbytes = cipher.encrypt(ciphertext.encode('utf8'))
    encodestrs = base64.b64encode(encryptedbytes)
    enctext = encodestrs.decode('utf8')
    return enctext

def get_stadium(periodID, stadiumID, token):
    payload = json.dumps({"periodId": periodID, "date": datetime.datetime.now().strftime('%Y-%m-%d'), "stadiumId": stadiumID})
    timestamp = int(time.time()*1000)
    header = {
        'Host': 'tyb.qingyou.ren',
        'Connection': 'keep-alive',
        'Content-Length': '49',
        'resultJSON': str(timestamp),
        'referer': 'https://servicewechat.com/wxebade4c4672d5e61/13/page-frame.html',
        'xweb_xhr': '1',
        'resultJSONSignature': getsig(str(timestamp)),
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6763',
        'token': 'cb9eb08f-26b3-4984-bcfb-a8a583b53482',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN, zh'
    }
    url = 'https://tyb.qingyou.ren/user/book/'
    r = requests.post(url, data=payload, headers=header)
    print(r.text)
    time.sleep(2)  # 经测试不能连续发送必须间隔两秒

if __name__ == '__main__':
    token = ''
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(now)
        if now == '12:00:00':
            break
    get_stadium(periodID = 2, stadiumID = 1, token = token) #大概率只抢的到一个，后面看运气
    get_stadium(periodID = 3, stadiumID = 1, token = token)
    get_stadium(periodID = 4, stadiumID = 1, token = token)

'''periodID
2 -> 16:00-17:00 
3 -> 17:00-18:00 
4 -> 18:00-19:00 
5 -> 19:00-20:00 
6 -> 20:00-21:00 
'''
'''stadiumID
1 -> 仙林羽毛球1号场地
2 -> 仙林羽毛球2号场地
3 -> 仙林羽毛球3号场地
4 -> 仙林羽毛球4号场地
5 -> 三牌楼羽毛球1号场地
6 -> 三牌楼羽毛球2号场地
7 -> 三牌楼羽毛球3号场地
8 -> 三牌楼羽毛球4号场地
13 -> 三牌楼羽毛球5号场地
14 -> 三牌楼羽毛球6号场地
'''
