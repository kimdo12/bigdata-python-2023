#변수에 대하여


a=1
b='python'
c=[1,2,3]

# print(id(a))
# print(id(b))
# print(id(c))


# 문자열은 할당, copy 동일/ 리스트 할당, copy가 다름

a= b
print(id(a))
print(id(b))
print(a is b)

print(b)
print(a)

from copy import copy

a = copy(b)
print(id(a))
print(id(b))
print(a is b)

a,b = ('python', 5)
print(a)
[c,d] = ['python', 7] #이렇게는 많이 안씀


