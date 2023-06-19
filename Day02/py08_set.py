#집합

s1= set([1,2,3,4,5,1,2,3])
print(s1) #결과 12345 중복 허용x

s2 = set((3,6,9,12,3,12,15))
print(s2)

s3= set('Hello')
print(s3)

print(list(s3)) #집합이 리스트로 변경
print(tuple(s3)) #집합이 튜플로 변경