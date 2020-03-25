import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
rank = soup.select('#body-content > div.newest-list > div > table > tbody > tr > td.number')
name = soup.select('#body-content > div.newest-list > div > table > tbody > tr > td.info > a.title.ellipsis')
singer = soup.select('#body-content > div.newest-list > div > table > tbody > tr > td.info > a.artist.ellipsis')

# movies (tr들) 의 반복문을 돌리기
for item in zip(rank, name, singer):
    print(item[0].text.split('\n')[0].strip(),".",item[1].text.strip(),"-",item[2].text.strip())
#############################