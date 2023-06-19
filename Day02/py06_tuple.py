# 튜플
# 리스트와 유사하지만 추가, 수정, 삭제가 불가 immutable

t1 = (1,2,3)

print(t1[2])
print(t1[:3]) #마지막값의 인덱스 +1 까지 출력


t2= (5,6,7)
t3 = t1+t2 #새로운 튜플을 최초에 만드는 연산은 간으
print(t3)

def calc(x,y): #값을 한꺼번에 여러개 리턴 받을 수있음 (java, C#, python 동일)
    #사칙 연산 모두 다 처리
    add=x+y
    minus =x-y
    mult =x*y
    div= x/y
    return (add,minus, mult , div)
res1, res2,res3, res4 = calc(5,8)
print (res1, res2,res3,res4)