import requests
from bs4 import BeautifulSoup
import re

# 发送GET请求获取网页内容
url = 'https://www.qingting.fm/radios/20500187/'
response = requests.get(url)

# 解析网页内容
soup = BeautifulSoup(response.content, 'html.parser')

# 查找所有的链接
links = soup.find_all('a', href=True)

# 输出所有链接
for link in links:
    href = link['href']
    # 如果链接是相对路径，转换为绝对路径
    if not href.startswith('http'):
        href = url + href
    print(href)