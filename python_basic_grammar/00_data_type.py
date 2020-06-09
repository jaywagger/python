#ctl+1
#ctl+`

# 출력해보기
print('Hello World!')

# 프로그래밍 언어의 기본 3가지
# 1. 변수 저장 - 무엇을 저장할 수 있을까?
number = 10
string = '10'
boolean = True #시작을 대문자로
#파이썬에는 값이 없다는 뜻인 None 타입이 존재
nothing = None #시작을 대문자로
print(number, string, boolean, nothing)
print(type(nothing)) #타입 확인

# 1.1 정수형 
number = 10
float_num = 1.3
complex_num = (3+3j)
print(type(number),type(float_num),type(complex_num))

#2. Boolean
print(type(True))
print(type(False))
# 0, 0.0, [], {} => False로 표현된다.
print(False == 0) #False와 0이 같은지에 대한 True 즉 둘이 같다

# 3. 문자형
# '', ""
text1 = 'hi'
test2 = "kim"
print(text1,test2) 
print(type(text1),type(test2))

#문자열 입력 받기 - input
age = input("나이를 입력해 주세요 : ") # string값
print(age)

#String 을 Int로 변경
print(type(age))
print(int(age))
print(type(int(age)))

#string interpolation - 보관법
name = 'kim'
print('안녕하세요,',name)
print('{}, {}'.format(text1,name))
print(f'{text1}, {test2}') #3.6버전 이상부터

#연산과 출력 형태 지정
pi = 3.141592
print(f'원주율은 {pi}. 반지름 = 2 원의 넚이는 {pi*2*2}') #연산가능 #변수 출력도 가능
print(f'원주율은 {pi:.4}. 반지름 = 2 원의 넚이는 {pi*2*2}')