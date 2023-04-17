from Crypto.Cipher import AES
import requests
import base64
import json
import time

url = 'https://tyb.qingyou.ren/user/book/'
timestamp = int(time.time()*1000)


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


header = {
    'Host': 'tyb.qingyou.ren',
    'Connection': 'keep-alive',
    'Content-Length': '49',
    'resultJSON': str(timestamp),
    'referer': 'https://servicewechat.com/wxebade4c4672d5e61/13/page-frame.html',
    'xweb_xhr': '1',
    'resultJSONSignature': getsig(str(timestamp)),
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6763',
    'token': 'ecd8e127-ba01-4db6-9175-c63622ac08b0',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN, zh'
}

payload = json.dumps({"periodId": 28, "date": "2023-04-17", "stadiumId": 9})
result = requests.post(url, data=payload, headers=header)
print(result.content)
