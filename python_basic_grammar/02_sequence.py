# 02_sequence.py
# 데이터가 순차적으로 나열이 되어있다.
# 주의할 점: 정렬되어 있다는 뜻은 아님
# list, tuple, range, string
# 1. list
print('------1.list---------')
list_a = []
list_b = list()
list_a = ['삼성',23,True]
print('-------1.1index로 접근하기--------')
# 1-1. index로 접근하기
print(list_a[0])
print(list_a[1])
print(list_a[-1]) #맨뒤 출력
print('------2. Tuple--------')
# 2. Tuple
tuple_a = ()
tuple_a = (1,2)
print(tuple_a)
print('---값을 하나만 넣고자 한다면---')
#값을 하나만 넣고자 한다면
tuple_b = (1,)
tuple_c = (1)
print(tuple_b)
print(tuple_c)
print('-------3. range--------')
#3. range
print(range(10))
print(type(range(10)))
print(list(range(10)))
print(list(range(3,10,2))) #3~9 출력 2씩 건너뛰기
