# 함수
def add(x,y):
    result = x+y
    return result

def add(x,y) -> int:
     return x+y
def minus(x,y):
     return x-y

print(minus(6,2))
print(add(3,4))
print(add('Hello','World')) #입력 파라미터에 제약이 없음

# 리턴값이 함수
def plus(x,y)-> None:
     print(x+y)

plus(3, 5.4)
print(None) #Null, null

def add_many(*args):
     result =0
     for i in args:
          result +=i
     return result

print(add_many(1,2,3))
print(add_many(3,6,9,12,15,18,21))
print(add_many(1,2,3,4,5,6,7,8,9,10))
# print(add_many('Life','is','short','you','need','Python'))

# 키워드 매개변수
def print_kwargs(**kwargs):
     print(kwargs)

print_kwargs(a=1)
print_kwargs(name='kim', age=27)

def all_calc(x,y):
     return (x+y, x-y,x*y, x/y)

print(all_calc(601,45))
(res_add, res_min, res_mul, res_div)= all_calc(601,45)


# 함수 기본값
def introduce_myself(name,old, man=True) -> None:
     print(f'나의 이름은 {name} 입니다')
     print(f'나이는 {old} 입니다')
     if man:
          print('나는 남자입니다')
     else:
          print('나는 여자입니다.')

introduce_myself('유숙', 45, False)
introduce_myself(man=False, name='애슐리', old=40)

val =1
def valtest(val): #지역변수
     val+=1
valtest(val)
print(val)

def valtest2():
    global val # 전역변수 val을 내가 함수내에서 잠시 가져다씀
    val += 10

res = valtest(val)
print(val)
print(res)

valtest2()
print(val)

# lambda 함수

#javascript jQuery
# $(document).ready = function(){ 
# }
# $(document).ready = ()=>{// lambda함수}
#}
adds = lambda a, b: a+b
# def adds(a,b):
#      return a+b
print(adds(6,7))

print(abs(-3)) #절대값 abd[olute]
print(all([1,3,5,7,9,2,4,6,8]))
