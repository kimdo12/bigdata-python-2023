#딕셔너리

iron_man ={'name':'Tony Stark', 'address':'New york', 'armer':'Repluser Arm'}
print(iron_man)

# print(iron_man.get('name'))
# print(iron_man['name'])

# d1 = { 1:'a', 1:'b'}
# print(d1) # 중복 허용x
# d2 = {1:'test', 2:'test'}

print(iron_man.keys())
for item in iron_man.keys():
    print (item)
    print(iron_man.values())


    print(iron_man.items())