# A first python script
# import sys
# import myfile
# print (myfile.title)
# print(sys.platform)
# print(2**100)
# x = 'Spam!'
# print(x*8)
# print(dir(myfile))
# s = 'spam'
# print(s[-2])
# print(s[1:3]) #左闭右开
# print(s[1:]) #[1,无穷大）
# print(s)
# c = s +"xyz"
# print(c)
# print(c.find('xyz'))
# import re
# match = re.match('Hello[ \t]*(.)*world', 'Hello    Python world')
# print(match.group(1))
# print(type(s))

# print(40 + 3.2)
# import math
# import random
# print(math.sqrt(144))
# print(144**0.5)
# print(pow(144,0.5))
# ma = random.random()
# print(ma)
# sa = random.randint(1,10)
# print(sa)
#
# la = random.choice(['aaaa','bcccc','ccasa'])
# print (la)

list = [11,23,42,73,12,51]
a = {'a':1,'b':2}

#enumerate()函数，会将数组或列表组成一个索引序列
for index, text in enumerate(list):
  print (index ,text)