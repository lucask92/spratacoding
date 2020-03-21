import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

name = soup.select('#old_content > table > tbody > tr > td.title > div > a')
rank = soup.select('#old_content > table > tbody > tr > td.point')
for item in zip(name, rank):
    print(item[0].text, item[1].text)
