#module 'mymod'

print("hello world")

'''
    this is a comment
    multiline
'''

# one line comment
# substring
print("hello"[0:4])

print(99)

print(5, 7, 9, "same line")

# raw text
print(r'c:\butt\n')

# variable
myvariable = "Hello mike"
myvariable = "Hello everyone"  # overwrite

myInt = 34
myFloat = 56.6

alist = [4, 5, "seven"]
adictionary = {"mike": 4, "pete": 6}

print(type(myvariable))
print(type(myInt))
print(type(myFloat))
print(type(alist))
print(type(adictionary))

# concat strings
myvariable += ' frends'
print(myvariable)

# conditionals: indents matter
x = 6

if x > 0:
    pass

if x < 5:
    print("true")
else:
    print("false")

color = 'red'

if color == 'red':
    print('color is red')
elif color == 'blue':
    print('color is blue')

# nested if
if x == 6:
    if color == 'red':
        print('x is 6 and color is red')

if color == 'red' and x == 6:
    print('color is red and x is 6')

# looping

people = ['mike', 'bob', 'steve', 'carl']

for person in people:
    print(person)

for i in range(0, 3):
    print(people[i])

#remove i from scope
del i

# while
count = 7

while count >= 0:
    print("counter is", count)
    count -= count

# function
# note: parameters are passed as a copy (immutable)


def sayHello(name='carl'):
    'this is a comment it gets ignored'
    print('hello', name)


sayHello('john')


def getSum(num1, num2):
    total = num1 + num2
    return total


print('getSum =', getSum(5, 10))

# parameter gets modified (called a method on object)


def addToList(myl):
    myl.append(5)
    print(mylist)


mylist = [4, 5, 6, 7]

addToList(mylist)

print(mylist)

#string methods
name = 'Hello world'

print('capitalize', name.capitalize())
print('swapcase', name.swapcase())
print(len(name))
#count characters
print(name.count('l'))

print(name.startswith('Hello'))
#split
print(name.split(' '))

#seach
print(name.find('wo'))

#index error if not found
print(name.index('H'))

#is it alphabetic, alphanumeric
print(name.isalpha())