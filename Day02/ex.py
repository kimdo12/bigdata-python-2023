hong={'국어':80,'영어':75, '수학':55}
average = sum(hong.values()) / len(hong)
print(average)
# sum =0
# for item in hong.values():
#     sum += item
# print(f'홍길동의 평균점수는 {sum/len(hong)}')
#===================================================
a =13
if a %2==0 :print('짝수')
else:print('홀수')
# result = a%2 ==0
# print(result)
#===================================================
pin ="881120-1068234"
# yyyymmdd='19'+pin[0:6]
yyyymmdd='19'+pin.split('-')[0]
# num = pin[7:14]
num = pin.split('-')[1]
print(yyyymmdd)
print(num)
#===================================================
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)
#===================================================
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b= list(aSet)
print(b)