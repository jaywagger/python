#01_operations.py
#논리 연산자
#and, or, not
print("______and______") # 둘다 true 일 때 true
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print("______or______") #둘 중 하나만 true 여도 true
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("______not______") #반대 cnffur
print(not True)
print(not False)

print("______in, not in______") #반대 cnffur
print('a' in 'apple')
print(1 not in [1,2,3])


print("___________단축 평가___________")
#  값 없음므로 false, text는 true, 그 뒤로 연산 안함
print(''or'text'or'text2')
print('text'and''or'text2')
