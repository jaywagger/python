import requests 
import pprint
# 아래 콘솔창에 pip install requests 하면 다운이 된다. 
key = 'AIzaSyBN34BLlyicen7IBwvvOV1_L_2WLxarnGE'
#string interpolation
search = input("검색어를 입력해 주세요: ")
q = f'q={search}'
my_type = 'type=video'
part = 'part=snippet'
url = f'https://www.googleapis.com/youtube/v3/search?key={key}&{part}&{my_type}&{q}&maxResults=20' 
#           기본주소, search, ?, key, part, type, query
# 1. 검색어를 입력하기 위한 parameter
# 2. 영상들을 검색할 것
# 3. 그 영상들의 제목과 채널명

print(url)

response = requests.get(url)
# print(response)
#상태코드 200: 정상
datas = response.json()  #파이썬에서 사용할 수 있도록 타입(dictionary)을 변경해야 함
# print(type(data))
#읽기 어려움. import pprint (pretty print)

#채널명, 영상 제목
for data in datas['items'][:10]:
    # print(data['snippet']['title'],data['snippet']['channelTitle'])
    print(data['snippet']['title'], end=' 채널명 ')
    print(data['snippet']['channelTitle'])


