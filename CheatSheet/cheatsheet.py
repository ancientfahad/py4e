# IO - Input Output
username = input('Type your username: ')
print(username)

# Input
first_name = input('Type your first name: ')
last_name = input('Type your last name: ')

# Output
print('Welcome', first_name, last_name)

# Iteration
# While loop
n = 5

while n > 0:
    print(n)
    n = n - 1

print('Blastoff!')

x = 15
x = x + 5
print(x)

# While loop
while True:
    line = input('> ')
    if line == 'done':
        break
    if line == 'Done':
        continue
    print(line)
print('Done!')

# Iteration
# For loop
for i in range(5):
    print(i)

    if i > 2:
        print('i greater than 2')

    print('Done with i', i)

print('All done')

# For loop
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff')

for x in range(1, 6):
    print(x, end='', flush=True)  # Printing without newline

# Conditional Statements & Comparison Operators
x = 5

if x == 5:
    print('Equals')
    x = x + 1
    print('Tab')
    print('Space')
if x > 5:
    print('Greater than')
if x >= 5:
    print('Greater than or equals')
if x < 7:
    print('Less than')
if x <= 7:
    print('Less than or equals')
if x != 7:
    print('Not equals')

x = 4

if x > 5:
    print('x greater than 5')
elif x < 5:
    print('x less than 5')
else:
    print('x equals to 5')

# try except
astr = 'Fahad'

try:
    istr = int(astr)
except Exception as e:
    istr = -1
print('first', istr)

astr = '123'

try:
    istr = int(astr)
except Exception as e:
    istr = -1
print('second', istr)


# Function
def main():
    print('main')


def second_main():
    print('second main')
    main()


second_main()


def print_input(usr_input):
    print('Hello', usr_input)


print_input(input('Type your name: '))


def get_usr_input():
    usr_input = str(input('Type your name: '))
    return usr_input


print(get_usr_input())


def addition(num1, num2):
    num3 = num1 + num2
    print(num3)


addition(int(input('Enter first number: ')), int(input('Enter second number: ')))


def stuff():
    print('Hello')
    return
    print('World')


stuff()


def addtwo(a, b):
    added = a + b
    return a


x = addtwo(2, 7)
print(x)

#  * * *  Library  * * *
# String Library

# .lower()
# .upper()
sample_string = input('Type your name: ')
print(sample_string)
lower_sample_string = sample_string.lower()
print(lower_sample_string)
upper_sample_string = lower_sample_string.upper()
print(upper_sample_string)

# .replace()
# .search()
# .find()
greet = 'Hello Fahad'
replaced_greet = greet.replace('Fahad', 'Anannya')
print(replaced_greet)

position = replaced_greet.find('Anannya')
print(position)

# .lstrip()
# .rstrip()
greet = '   Hello Fahad   '
print('lstrip', greet.lstrip())
print('rstrip', greet.rstrip())
print('strip', greet.strip())

# Prefixes
# .startswith()
greet = 'Hello Anannya'
print(greet.startswith('Hello'))
print(greet.startswith('H'))
print(greet.startswith('hello'))
print(greet.startswith('h'))

# Parsing and Extracting
data = 'From fahad.chowdhury@aisdhaka.org Sat Jan  5 09:14:16 2008'

at_position = data.find('@')
print(at_position)

space_position = data.find(' ', at_position)
print(space_position)

host = data[at_position + 1: space_position]
print(host)

x = 'From marquard@uct.ac.za'
print(x[14:17])

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos + 3])


# Global variable
def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)

# Length
fruit = 'banana'
print(len(fruit))

# Looping through strings
index = 0

while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

print('While done!')

for letter in fruit:
    print(letter)

print('For done!')

# Looping and counting
count = 0
fruit = 'banana'

for letter in fruit:
    if letter == 'a':
        count = count + 1

print(count)

# Slicing strings
input_str = 'Cheat Sheet'

print(input_str[0:1])
print(input_str[0:6])
print(input_str[6:12])

print(input_str[:2])
print(input_str[2:])

# String concatenation
str1 = 'Cheat'
str2 = 'Sheet'

print(str1 + ' ' + str2)

# Use of in
fruit = 'banana'

print('n' in fruit)

if 'a' in fruit:
    print('found')

# String comparision
fruit = 'banana'
fruit1 = 'banana'
fruit2 = 'mango'

if fruit == fruit1:
    print('Match')

if fruit != fruit2:
    print('Don not match')

if fruit1 < fruit2:
    print('fruit1 smaller than fruit2', len(fruit1), len(fruit2))

if fruit < fruit1:
    print('fruit smaller than fruit1', len(fruit), len(fruit1))
else:
    print('fruit equals to fruit1', len(fruit), len(fruit1))

if 'a' > 'A':
    print('a > A')
else:
    print('A > a')

if 'apple' > 'Apple':
    print('apple > Apple')
else:
    print('Apple > apple')

# Newline Character
message = 'Hello\nWorld'
print(message)

# Get current working directory and get all files in that directory
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

# Opening a file
file_handler = open('/Users/u75530/PycharmProjects/Assignments/mbox-short.txt')  # Specify file directory
file_handler1 = open('mbox-short.txt')  # Open from the current directory

file_name = input('Enter file name: ')

if '.txt' not in file_name:
    file_name = file_name + '.txt'


# print(file_handler)
# print(file_handler1)


# Printing data's of the file
def read_data():
    for text in file_handler2:
        text = text.rstrip()
        # if text.startswith('From'):
        # if not text.startswith('From'):
        if '@uct.ac.za' not in text:
            continue
        print(text)

    # read_file = file_handler1.read()
    # print(len(read_file))
    # print(read_file)
    # print(read_file[:20])


try:
    file_handler2 = open('/Users/u75530/Documents/' + file_name)
    print(file_name)
    read_data()
except Exception as e:
    print('File not found', e)
