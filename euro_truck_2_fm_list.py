import requests
from scapy.all import *

# # 发送一个简单的GET请求到蜻蜓FM网站
# response = requests.get('https://www.qingting.fm/radios/20500187/')

# # 打印响应内容
# # print(response.text)

# # 定义抓包回调函数
# def packet_callback(packet):
#     if packet.haslayer(TCP):
#         src_ip = packet[IP].src
#         dst_ip = packet[IP].dst
#         src_port = packet[TCP].sport
#         dst_port = packet[TCP].dport
#         print(f"TCP Packet from {src_ip}:{src_port} to {dst_ip}:{dst_port}")

# # 开始抓包
# sniff(prn=response.text, filter="tcp", count=10)


import requests
from bs4 import BeautifulSoup
import re

# 发送 GET 请求获取网页内容
url = 'https://www.example.com'
response = requests.get(url)

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(response.content, 'html.parser')

# 查找所有的 <img> 标签
img_tags = soup.find_all('img')

# 提取每个图片的 URL
for img in img_tags:
    img_url = img['src']
    print(img_url)

# 查找所有的 <video> 标签
video_tags = soup.find_all('video')

# 提取每个视频的 URL
for video in video_tags:
    video_url = video['src']
    print(video_url)
    