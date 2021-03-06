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
print(ord('G'))

# Get ASCII value of a numeric
print(chr(72))

# What word does the following sequence of numbers represent in ASCII:
# 108, 105, 110, 101

sample_list = [108, 105, 115, 116]
output = ''

for num in sample_list:
    output = output + chr(num)

print(output)

# XML
import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))

# json
import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

# Gives back an object which is almost like python dictionary
info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

# Goes to the json library -> loads string -> parse data
info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)

import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('   * No status found')
            continue
        s = u['status']['text']
        print('  ', s[:50])

sys.stdout.write("\033[F") #back to previous line
sys.stdout.write("\033[K") #clear line
