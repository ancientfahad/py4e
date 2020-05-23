# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers
# in the file and compute the sum of the numbers.

# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the
# other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_533489.txt (There are 98 values and the sum ends with 782)

# These links open in a new window. Make sure to save the file into the same folder as you will be writing your
# Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data
# file for analysis.

# Data Format
# The file contains much of the text from the introduction of the textbook except that random numbers are inserted
# throughout the text. Here is a sample of the output you might see:

# Why should you learn to write programs? 7746
# 12 1929 8827
# Writing programs (or programming) is a very creative
# 7 and rewarding activity.  You can write programs for
# many reasons, ranging from making your living to solving
# 8837 a difficult data analysis problem to having fun to helping 128
# someone else solve a problem.  This book assumes that
# everyone needs to know how to program ...

# The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of
# numbers in each line (including none).

# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a
# regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
import re

file_name = 'regex_sum_533489.txt'
file_handler = open(file_name)
total = 0

for line in file_handler:
    data = re.findall('[0-9]+', line)

    if len(data) > 0:
        for numbers in range(len(data)):
            total = total + int(data[numbers])

print('Sum:', total)

# Optional: Just for Fun
# There are a number of different ways to approach this problem. While we don't recommend trying to write the most
# compact code possible, it can sometimes be a fun exercise. Here is a a redacted version of two-line version of this
# program using list comprehension:

# Python 2
# import re
# print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )

# Python 3:
# import re
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )

# Please don't waste a lot of time trying to figure out the shortest solution until you have completed the homework.
# List comprehension is mentioned in Chapter 10 and the read() method is covered in Chapter 7.

# ********************************************************************************************************************
# ********************************************************************************************************************
# ********************************************************************************************************************

# Exploring the HyperText Transport Protocol
# You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response
# headers.

# http://data.pr4e.org/intro-short.txt

# There are three ways that you might retrieve this web page and look at the response headers:

# Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data.
# Make sure to change the code to retrieve the above URL - the values are different for each URL.

# Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are
returned.
Use the telnet program as shown in lecture to retrieve the headers and content.

# Enter the header values in each of the fields below and press "Submit".
import socket
import re

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

my_socket.send(cmd)

while True:
    data = my_socket.recv(1024)

    if len(data) < 1:
        break

    last_modified = re.findall('Last-Modified: (.+)\r', data.decode())[0]
    eTag = re.findall('ETag: "(.+)"\r', data.decode())[0]
    content_length = re.findall('Content-Length: (.+)\r', data.decode())[0]
    cache_control = re.findall('Cache-Control: (.+)\r', data.decode())[0]
    content_type = re.findall('Content-Type: (.+)\r', data.decode())[0]

    print(data.decode())

my_socket.close()

print('Last-Modified:', last_modified)
print('ETag:', eTag)
print('Content-Length:', content_length)
print('Cache-Control:', cache_control)
print('Content-Type:', content_type)

# ********************************************************************************************************************
# ********************************************************************************************************************
# ********************************************************************************************************************

# Scraping Numbers from HTML using BeautifulSoup
# In this assignment you will write a Python program similar to
# http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below,
# and parse the data, extracting numbers and compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the
# other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_533491.html (Sum ends with 96)

# You do not need to save these files to your folder since your program will read the data directly from the URL.
# Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

# Data Format

# The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like
# the following:

# <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
# <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
# <tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

# You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.

# Look at the sample code provided. It shows how to find all of a certain kind of tag, loop through the tags and
# extract the various aspects of the tags.

# ...
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#    # Look at the parts of a tag
#    print 'TAG:',tag
#    print 'URL:',tag.get('href', None)
#    print 'Contents:',tag.contents[0]
#    print 'Attrs:',tag.attrs

# You need to adjust this code to look for span tags and pull out the text content of the span tag, convert them to
# integers and add them up to complete the assignment.

# Sample Execution

# $ python3 solution.py
# Enter - http://py4e-data.dr-chuck.net/comments_42.html
# Count 50
# Sum 2...

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

numbers = list()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')

for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
    numbers.append(int(tag.contents[0]))

print('Sum =', sum(numbers))

# ********************************************************************************************************************
# ********************************************************************************************************************
# ********************************************************************************************************************

# Following Links in Python
# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The
# program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat
# the process a number of times and report the last name you find.

# We provide two files for this assignment. One is a sample file where we give you the name for your testing and the
# other is the actual data you need to process for the assignment

# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the
# last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah

# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Tygan.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is
# the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: B

# Strategy
# The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you
# to do the assignment without writing a Python program. But frankly with a little effort and patience you can
# overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But
# that is not the point. The point is to write a clever Python program to solve the program.

# Sample execution
# Here is a sample execution of a solution:

# $ python3 solution.py
# Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Enter count: 4
# Enter position: 3
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html
# The answer to the assignment for this execution is "Anayah".

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

process_count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def open_url(get_url, get_count, get_position):
    html = urllib.request.urlopen(get_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    retrieve_tags(soup, get_count, get_position)


def retrieve_tags(get_soup, get_count, get_position):
    # Retrieve all of the anchor tags
    tags = get_soup('a')

    get_last_name(tags, get_count, get_position)


def get_last_name(get_tags, get_count, get_position):
    global process_count

    for i in range(get_position):
        if i == (get_position - 1):
            print('Retrieving:', get_tags[i].get('href', None))
            third_url = get_tags[i].get('href', None)

    process_count = process_count + 1

    last_name = re.findall('.*_(.*).html', third_url)[0]

    if process_count != get_count:
        open_url(third_url, get_count, get_position)
    else:
        print(last_name)


input_url = input('Enter URL: ')
input_count = int(input('Enter count: '))
input_position = int(input('Enter position: '))

open_url(input_url, input_count, input_position)
