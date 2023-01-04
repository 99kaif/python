# function to variable
'''
def a():
    print("hello world")
b=a
a()
b()

write=print
write('hello')
'''

#higher order function

#part 1
'''
def cap(text):
    return text.upper()
def lower(text):
    return text.lower()
def high(func):
    ans=func('Hello')
    print(ans)
high(cap)
high(lower)
'''

#part2

def divisor(x):
    def dividend(y):
        return y/x
    return dividend
divide=divisor(5)
print(divide(50))