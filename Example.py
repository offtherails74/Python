# W03D2 Basic Data Types
# Addition
num1 = 10
num2 = 20
total = num1 + num2
print(total)
print (type(total))

# Multiplication and Division
height = 6
mass = 180
bmi = (mass / (height*height))
print (bmi)
print (type(bmi))

# Strings
name = "Dan"
surname = "Courcelles"
fullname = name + " " + surname
print (surname)
print (surname[0])
print (name + surname)
print (type(name))
print (name*10)

# Longer Strings
greeting = ("Hello, my name is " + name)
print (greeting)
print (type(greeting))

# Lists
emptyList = []
heights = [180, 170, 160, 150, 140]
print (heights)
print (heights[1])
heights2 = (heights [2:5])
all_list = heights + heights2
print (all_list)
print (type(all_list))

# tuples
empty_tuple = ()

#dictionaries
dict ()
dict_height = {"name": "Dan", "age": 25, "height": 180}
print (dict_height)
print (dict_height["name"])
print (dict_height["age"])
print (dict_height["height"])
print (type(dict_height))

# if
if bmi < 18.5:
    print ("Underweight")
if bmi >= 18.5 and bmi < 25:
    print ("Normal")
if bmi >= 25 and bmi < 30:
    print ("Overweight")
if bmi >= 30:
    print ("Obese")

# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x

# if/else - elif
x = 20


if x < 50:
     print('(first suite)')
     print('x is small')
else:
     print('(second suite)')
     print('x is large')


x = 120

if x < 50:
     print('(first suite)')
     print('x is small')
else:
     print('(second suite)')
     print('x is large')


name = 'Joe'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Joe':
    print('Hello Joe')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

names = {
    'Fred': 'Hello Fred',
    'Xander': 'Hello Xander',
    'Joe': 'Hello Joe',
    'Arnold': 'Hello Arnold'
}

print(names.get('Joe', "I don't know who you are!"))

print(names.get('Rick', "I don't know who you are!"))


raining = False
print("Let's go to the", 'beach' if not raining else 'library')

raining = True
print("Let's go to the", 'beach' if not raining else 'library')

age = 12
s = 'minor' if age < 21 else 'adult'
print (s)

y = 'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'
print (y)


# while loops
n = 5
while n > 0:
    n -= 1
    print(n)

# else
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')

# break
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')

# continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

# iterables
iter('foobar')                             # String

iter(['foo', 'bar', 'baz'])                # List

iter(('foo', 'bar', 'baz'))                # Tuple

iter({'foo', 'bar', 'baz'})                # Set

iter({'foo': 1, 'bar': 2, 'baz': 3})       # Dict

#____________________________________________________________________________________
a = ['foo', 'bar', 'baz']

itr = iter(a)
print (a)

next(itr)
next(itr)
next(itr)


# range
x = range(5)
print (x)

for n in x:
    print(n)
    
