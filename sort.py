#sort in list
'''
l=[ ['a',34,4],
    ['n',5,67],
    ['v',66,1] ]
# data = lambda x:x[1]
# l.sort(key=data)
# print(l)
data = lambda x:x[2]
l.sort(key=data,reverse=True)
print(l)
'''
#sort in tuple

t=( ['a',34,4],
    ['n',5,67],
    ['v',66,1] )
data=lambda x:x[0]
sorted_t=sorted(t,key=data,reverse=True)
print(sorted_t)