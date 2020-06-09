# 1. dictionary: key and value
print('Dictionary')
dict_a = {}
dict_b = dict()
# key가 중복이 불가능 하다.
dict_a = {'삼성':100, '역삼':50, '삼성':30} #뒤에가 덮어써진다
print(dict_a)

print('---------------')
print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())

print('---------------')
print(dict_a['삼성'])
print(dict_a.get('삼성'))

print('---.get과 []의 접근 차이점---')
dict_a = {'삼성':100, '역삼':50}
print(dict_a.get('선릉')) #값이 없다고 보여줌
#print(dict_a['선릉']) #에러가 떠서 멈추는 경우

print('------2. set-----')
#set는 순서가 없이 저장된다
set_a = {1,3,2}
set_b = {3,6,9}
print(set_a - set_b) #차집합
print(set_a | set_b) #합집합
print(set_a & set_b) #교집합

list_a = [1,1,1,1]
print(list(set(list_a))[0]) #중복 없애기

print('----불가편성----')
string ="immutable"
list_a = ['immutable?','real?']

print(string[0])
print(list_a[0])

list_b = list_a
