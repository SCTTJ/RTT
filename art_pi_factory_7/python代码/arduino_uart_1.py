import time
from pyb import UART
import ujson
import ubinascii
import pyb
import urequests as requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【官网获取的AK】&client_secret=【官网获取的SK】'
response = requests.get(host)
if response:
    print(response.json())
uart = UART(3, 19200)

while(True):
    uart.write("Hello World!\n")
    if (uart.any()):
        img = uart.read()
            # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=6kbvF4gXOvO3xuQplt3RSk7G&client_secret=taSQngCaay48FG3LTqZ4dyMm7qekZydf'
    response = requests.get(host)
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/driver_behavior"
    # 二进制方式打开图片文件
    #f = open('example.jpg', 'rb')
    params = {"image":img}
    access_token = response.json()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
    print (response.json())
    time.sleep(1000)
