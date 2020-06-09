#리스트 짜르기
sample_list = list(range(31))
print(sample_list[3])
print(sample_list[3:24])
print(sample_list)
print(sample_list[5:-1]) #이전 마지막에서 -1
print(sample_list[5:]) #5부터 끝까지
print(sample_list[3:len(sample_list):2]) #3~29까지 2개씩 건너뛰고

print('---생략하기---')
print(sample_list[:13:2])
print(sample_list[::2])
print(sample_list[::-1])