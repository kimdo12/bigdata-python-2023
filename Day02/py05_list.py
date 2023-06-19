#리스트
a =[1,2,3]
#자료구조 stack에 있는 pop 기능 구현
print(a)
print(a.pop())
print(a)

a.append(10)
print(a)

print(a.count(1)) #리스트안에 값이 몇개 있는지

# 리스트 확장
b = [4,5]
a.extend(b)
print(a)