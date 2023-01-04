l=[1,2,3,4,5,6]
#map
'''
data=lambda x:x*5
print(list(map(data,l)))
'''

#filter
'''
data=lambda x:x>=3
print(list(filter(data,l)))
'''

#reduce
import functools
data=lambda x,y:x+y
print(functools.reduce(data,l))