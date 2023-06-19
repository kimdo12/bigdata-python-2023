#제어문

money = True
if money==True:
    print('ㅋㅋ')
elif money==False:
    print('드가자')
else:
    print('asd')

print(3 in [1,2,4,5,6,7]) # 리스트안에 3이있는가

while(money ==False):
    print('asdddd')

print('\n\n\n')

for i in range(0,10):
        print(i)

l1=[1,3,4,5,7,9]
for i in l1:
     print(i)

for j in range(1, 10, 2): #2는 증가량
     print(j)

for x in range(2, 10 ): #2단 ~9단
     for y in range(1,10):
          print(f'{x}X{y}={x*y:2d}', end=' ')
     print('')      