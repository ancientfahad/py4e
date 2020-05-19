# # Finding Numbers in a Haystack
# # In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers
# # in the file and compute the sum of the numbers.
#
# # Data Files
# # We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the
# # other is the actual data you need to process for the assignment.
#
# # Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# # Actual data: http://py4e-data.dr-chuck.net/regex_sum_533489.txt (There are 98 values and the sum ends with 782)
#
# # These links open in a new window. Make sure to save the file into the same folder as you will be writing your
# # Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data
# # file for analysis.
#
# # Data Format
# # The file contains much of the text from the introduction of the textbook except that random numbers are inserted
# # throughout the text. Here is a sample of the output you might see:
#
# # Why should you learn to write programs? 7746
# # 12 1929 8827
# # Writing programs (or programming) is a very creative
# # 7 and rewarding activity.  You can write programs for
# # many reasons, ranging from making your living to solving
# # 8837 a difficult data analysis problem to having fun to helping 128
# # someone else solve a problem.  This book assumes that
# # everyone needs to know how to program ...
#
# # The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of
# # numbers in each line (including none).
#
# # Handling The Data
# # The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a
# # regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
# import re
#
# file_name = 'regex_sum_533489.txt'
# file_handler = open(file_name)
# total = 0
#
# for line in file_handler:
#     data = re.findall('[0-9]+', line)
#
#     if len(data) > 0:
#         for numbers in range(len(data)):
#             total = total + int(data[numbers])
#
# print('Sum:', total)
#
# # Optional: Just for Fun
#
# # There are a number of different ways to approach this problem. While we don't recommend trying to write the most
# # compact code possible, it can sometimes be a fun exercise. Here is a a redacted version of two-line version of this
# # program using list comprehension:
#
# # Python 2
# # import re
# # print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )
#
# # Python 3:
# # import re
# # print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
#
# # Please don't waste a lot of time trying to figure out the shortest solution until you have completed the homework.
# # List comprehension is mentioned in Chapter 10 and the read() method is covered in Chapter 7.

# # ********************************************************************************************************************
# # ********************************************************************************************************************
# # ********************************************************************************************************************

# Welcome Al Fahad D. Chowdhury from Using Python to Access Web Data

# Exploring the HyperText Transport Protocol
# You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response
# headers.

# http://data.pr4e.org/intro-short.txt

# There are three ways that you might retrieve this web page and look at the response headers:

# Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data.
# Make sure to change the code to retrieve the above URL - the values are different for each URL.

# Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
# Use the telnet program as shown in lecture to retrieve the headers and content.

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
