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

# List
colors = ['black', 'white', 'blue']
print(colors)

colors[1] = 'dark black'
print(colors)
print(len(colors))

print(range(len(colors)))

for i in range(len(colors)):
    color = colors[i]
    print(color)

# Concatenating Lists
colors1 = ['black', 'blue', 'green']
colors2 = ['white', 'yellow', 'red']

colors = colors1 + colors2

# print(len(colors1), len(colors2))
# print(range(len(colors1)), range(len(colors2)))

print(colors1)
print(colors2)
print(colors)

sliced_colors = colors[1:3]

print(sliced_colors)

# List from Scratch
new_list = list()
new_list.append('Fahad Chowdhury')
new_list.append('13/07/1994')
new_list.append('0+')
new_list.append('01617131994')

new_list.append(input('Type your name: '))
new_list.append(input('Type your dob: '))
new_list.append(input('Type your blood group: '))
new_list.append(input('Type your mobile number: '))

print(new_list)

# Sort Lists
country_list = ['Brazil', 'Argentina', 'Germany', 'Portugal', 'England']
country_list.sort()

print(country_list)

# Built in functions of list
numbers = [10, 4, 3, 8, 12, 20, 13, 7]
print(max(numbers), min(numbers), sum(numbers))

# Strings and Lists
message = 'With three words'
split_message = message.split()

message = 'With;three;words'
split_message = message.split(';')

print(split_message)

for word in split_message:
    print(word)

file_handler = open('/Users/u75530/Documents/' + 'mbox-short.txt')

for line in file_handler:
    line = line.rstrip()

    if not line.startswith('From '):
        continue
    else:
        split_line = line.split()
        email = split_line[1]
        split_email = email.split('@')
        host = split_email[1]

        print(host)

# Dictionary
user_information = dict()
user_information['name'] = 'Fahad Chowdhury'
user_information['dob'] = '13/07/1994'
user_information['bloodgroup'] = 'O+'
user_information['contact'] = '01617131994'

print(user_information)
print(user_information['name'])

name_dictonary = dict()
names = ['Fahad', 'Anannya', 'Messi', 'Ronaldo', 'Fahad', 'Anannya', 'Messi', 'Fahad']

for name in names:
    if name not in name_dictonary:
        name_dictonary[name] = 1
    else:
        name_dictonary[name] = name_dictonary[name] + 1

print(name_dictonary)

x = name_dictonary.get('Fahad', 0)

counts = dict()
names = ['Fahad', 'Anannya', 'Messi', 'Ronaldo', 'Fahad', 'Anannya', 'Messi', 'Fahad']

for name in names:
    counts[name] = counts.get(name, 0) + 1

print(counts)

file_handler = open('/Users/u75530/Documents/' + 'words.txt')

counts = dict()
for line in file_handler:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

for key in counts:
    print(key, counts[key])

print(list(counts))
print(counts.keys())
print(counts.values())
print(counts.items())

for counts_keys, counts_values in counts.items():
    print(counts_keys, counts_values)

stuff = dict()
print(stuff.get('candy', -1))

# Tuples
sample_tuple = ('Black', 'White', 'Red')
print(sample_tuple[2])

# Tuples vs Dictionary
d = dict()
d['brazil'] = 2
d['argentina'] = 1

for (t, s) in d.items():
    print(t, s)

tups = d.items()
print(tups)

d = {'brazil': 3, 'argentina': 1, 'germany': 4, 'portugal': 2}
# Sort by Keys
print(d)
print(d.items())

for (t, s) in sorted(d.items()):
    print(t, s)

# Sort by Values
tmp = list()
for (t, s) in sorted(d.items()):
    tmp.append((s, t))

tmp = sorted(tmp, reverse=True)

print(tmp)

file_handler = open('/Users/u75530/Documents/romeo.txt')
count = dict()
for line in file_handler:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

lst = list()
for key, val in count.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst:
    print(key, val)

d = {'brazil': 3, 'argentina': 1, 'germany': 4, 'portugal': 2}
print(sorted([(v, k) for k, v in d.items()]))

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])

# Regular Expression
import re

# re.search() returns T/F if string matches regex
# re.findall() returns the matching strings

sample_text = 'I finished my SSC on 2011, with a GPA of 4.75, with 5 A+'
sample_text = 'From: Using the: character'

find_num = re.findall('[0-9]+', sample_text)  # one or more digits
find_vowel = re.findall('[aeiouAEIOU]+', sample_text)  # one or more characters (vowel)

greedy_matching = re.findall('^F.+:', sample_text)
nongreedy_matching = re.findall('^F.+?:', sample_text)

print(find_num)
print(find_vowel)
print(greedy_matching)
print(nongreedy_matching)


def re_func():
    hand = open('/Users/u75530/Documents/mbox-short.txt')
    for line in hand:
        line = line.rstrip()

        # Search
        # if re.search('From: ', line):

        # Starts with F
        # if re.search('^From: ', line):

        # Starts with X - has any number of characters - has a colon (:)
        # if re.search('^X.*:', line):

        # Starts with X - has dash (-) - has any non-whitespace character - has a colon (:)
        if re.search('^X-\S+:', line):
            print(line)


def find_func():
    hand = open('/Users/u75530/Documents/mbox-short.txt')
    for line in hand:
        line = line.rstrip()
        if line.find('From: ') >= 0:
            print(line)


re_func()
find_func()

data = 'From fahad.chowdhury@aisdhaka.org Sat Jan  5 09:14:16 2008'

# Extracting email address using regex
email_address = re.findall('\S+@+\S+', data)  # \S+ one or more non-whitespace character
email_address = re.findall('^From (\S+@+\S+)', data)  # Parenthisis () extracts the data we want
print(email_address)

# Extracting host manually
at_position = data.find('@')
space_after_at_position = data.find(' ', at_position)
host = data[at_position + 1:space_after_at_position]
print(host)

# Extracting host with regex
# host = re.findall('@+(\S+)', data)
# host = re.findall('@([^ ]*)', data)  # [^ ] everything but space * one or more
host = re.findall('^From .*@([^ ]*)', data)  # .* any number of characters
print(host)

# Extracting host with dual split
data_split = data.split()
email = data_split[1]
email_split = email.split('@')
host = email_split[1]
print(host)

file_handler = open('/Users/u75530/Documents/mbox-short.txt')
count = 0
for line in file_handler:
    host = re.findall('^From .*@[^ ]*', line)
    email = re.findall('^From (\S+@+\S+)', line)

    if len(host) > 0:
        count = count + 1
        print(host)
print(count)

# X-DSPAM-
file_handler = open('/Users/u75530/Documents/mbox-short.txt')
data_list = list()

for line in file_handler:
    data = re.findall('^X-DSPAM-Confidence: (\S+)', line)
    data = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(data) > 0:
        data_list.append(float(data[0]))

print('Max:', max(data_list))

# Use of backslash \
data = 'This game will cost $10.00'
get_price = re.findall('\$[0-9.]+', data)
print(get_price)

# Sockets
import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

my_socket.send(cmd)

while True:
    data = my_socket.recv(512)

    if len(data) < 1:
        break
    print(data.decode())

my_socket.close()

import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

file_hander = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
file_hander = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
counts = dict()

for line in file_hander:
    print(line.decode().strip())

for line in file_hander:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)

url = input('Enter url: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all anchor tags
tags = soup('a')

for tag in tags:
    print(tag.get('href'), None)

import re

sample_string = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
href_string = re.findall('href="(.+)"', sample_string)
print(href_string)

# Get numeric value of ASCII character
print(ord('H'))

# Get ASCII value of a numeric
print(chr(72))

# What word does the following sequence of numbers represent in ASCII:
# 108, 105, 110, 101

sample_list = [108, 105, 110, 101]
output = ''

for num in sample_list:

    output = output + chr(num)

print(output)
