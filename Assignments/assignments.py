# Convert Elevator Floors
# Elevator number for Ground floor in Europe is 0
# Elevator number for Ground floor in US is 1

inp = input('Which floor you wanna go? Enter in Europe Style: ')
us_floor = int(inp) + 1
print('US Floor ', us_floor)

# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
# You should use input to read a string and float() to convert the string to a number.

hrs = input('Enter Hours:')
rphrs = input('Enter Rate:')

gpay = float(hrs) * float(rphrs)

print('Pay:', gpay)

# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types numbers properly.

# Verify hours input
try:
    hours = int(input('Enter hours: '))
except Exception as e:
    print('Invalid hours', e)
    quit()

    # seek(0)

# Verify rate per hours input
try:
    rate_per_hrs = float(input('Enter rate per hours: '))
except Exception as e:
    print('Invalid rate', e)
    quit()

# Check for extra pay
if hours > 40:
    normal_pay = 40 * rate_per_hrs
    extra_hours = hours - 40
    extra_pay = extra_hours * (1.5 * rate_per_hrs)
    final_pay = extra_pay + normal_pay
else:
    final_pay = hours * rate_per_hrs

print(final_pay)

# Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

try:
    score = float(input('Enter score between 0.0 and 1.0: '))
except Exception as e:
    print('Invalid score!', e)

if score < 0.0 or score > 1.0:
    print('Invalid score. Score should be between 0.0 and 1.0')
    quit()
else:
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    elif score < 0.6:
        print('F')

# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the
# normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the
# logic to do the computation of pay in a function called computepay() and use the function to do the computation.
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should
# be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about
# error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your
# variable sum or use the sum() function.

# Verify input
hours = 0
rate_per_hrs = 0

while hours <= 0:
    # noinspection PyBroadException
    try:
        hours = int(input('Type hours in numbers: '))
    except Exception as e:
        print('Invalid hours')
        quit()

    if hours <= 0:
        print('Invalid hours')

while rate_per_hrs <= 0:
    # noinspection PyBroadException
    try:
        rate_per_hrs = float(input('Type rate per hours in numbers: '))
    except Exception as e:
        print('Invalid rate')
        quit()
    if rate_per_hrs <= 0:
        print('Invalid hours')


def computepay(ghours, grate_per_hrs):
    # Check for extra pay
    if ghours > 40:
        normal_pay = 40 * grate_per_hrs
        extra_hours = ghours - 40
        extra_pay = extra_hours * (1.5 * grate_per_hrs)
        return (extra_pay + normal_pay)
    else:
        return (ghours * grate_per_hrs)


print('Pay', computepay(hours, rate_per_hrs))

# Find the largest number in [9, 41, 12, 3 74, 15]

largest_number = 0

for number in [9, 41, 12, 3, 74, 15]:
    if number > largest_number:
        largest_number = number
    else:
        continue

print('largest number: ', largest_number)

# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. # Once 'done' is
# entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10,
# and 4 and match the output below.

smallest_number = None
largest_number = None


def get_user_input():
    while True:

        user_input = input('Enter a number: ')

        if user_input == 'done':
            break

        try:
            user_input = int(user_input)
            get_largest_number(user_input)
            get_smallest_number(user_input)
        except Exception as e:
            print('Invalid input')


def get_smallest_number(usr_input):
    global smallest_number

    if smallest_number is None:
        smallest_number = usr_input
    else:
        if usr_input < smallest_number:
            smallest_number = usr_input


def get_largest_number(usr_input):
    global largest_number

    if largest_number is None:
        largest_number = usr_input
    else:
        if usr_input > largest_number:
            largest_number = usr_input


get_user_input()

print('Maximum is', largest_number)
print('Minimum is', smallest_number)

# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475"

colon_position = text.find(':')
text_sliced = text[colon_position + 1:30]
text_striped = text_sliced.strip()

final_text = float(text_striped)

print(final_text)

# /Users/u75530/Documents/GitHub/CheatSheet

# Write a program that prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt
file_name = input('Enter file name: ')

if '.txt' not in file_name:
    file_name = file_name + '.txt'


def read_file(file_handler):
    rFile = file_handler.read().upper().rstrip()
    print_file(rFile)


def print_file(rFile):
    print(rFile)


try:
    file_handler = open('/Users/u75530/Documents/GitHub/' + file_name)
    read_file(file_handler)
except Exception as e:
    print('Invalid file name!')

# Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and
# compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# When you are testing below enter mbox-short.txt as the file name.
file_name = input('Enter file name: ')

count = 0
total_floating_point = 0


def read_file(file_handler):
    for data in file_handler:
        if data.startswith('X-DSPAM-Confidence:'):
            get_floating_point(data)


def get_floating_point(data):
    global count
    global total_floating_point

    colon_position = data.find(':')
    data_sliced = data[colon_position + 1:30]
    data_striped = data_sliced.strip()

    floating_point = float(data_striped)

    count = count + 1
    total_floating_point = total_floating_point + floating_point


try:
    file_handler = open('/Users/u75530/Documents/' + file_name)
    read_file(file_handler)
except Exception as e:
    print('Invalid file name!', e)

print('Average spam confidence:', total_floating_point / float(count))

# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the
# split() method. The program should build a list of words. For each word on each line check to see if the word is
# already in the list and if not append it to the list. When the program completes, sort and print the resulting
# words in alphabetical order. You can download the sample data at http://www.py4e.com/code3/romeo.txt
words_list = list()

file_handler = open('/Users/u75530/Documents/romeo.txt')

for line in file_handler:

    line = line.rstrip()
    line = line.split()

    for words in line:

        if words not in words_list:
            words_list.append(words)

words_list.sort()
print(words_list)

# Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the
# following line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 You will parse the From line using split()
# and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print
# out a count at the end. Hint: make sure not to include the lines that start with 'From:'. You can download the
# sample data at http://www.py4e.com/code3/mbox-short.txt

file_name = input('Enter filename: ')

if '.txt' not in file_name:
    file_name = file_name + '.txt'

try:
    file_handler = open('/Users/u75530/Documents/' + file_name)
except Exception as e:
    print('File not found!', e)
    quit()

count = 0

for line in file_handler:
    line = line.rstrip()

    if not line.startswith('From '):
        continue
    else:
        count = count + 1
        split_line = line.split()
        email = split_line[1]

        print(email)

print('There were', count, 'lines in the file with From as the first word')

# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the
# mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
# they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
# loop to find the most prolific committer.
emails = dict()
bigcount = None
bigsender = None


def find_emails(file_hander):
    for line in file_handler:
        if line.startswith('From '):
            datas = line.split()
            email = datas[1]
            emails[email] = emails.get(email, 0) + 1

    find_sender()


def find_sender():
    global bigcount
    global bigsender

    for sender, count in emails.items():
        if bigcount is None or count > bigcount:
            bigcount = count
            bigsender = sender


file_name = input('Enter filename: ')

if '.txt' not in file_name:
    file_name = file_name + '.txt'

try:
    file_handler = open('/Users/u75530/Documents/' + file_name)
    find_emails(file_handler)
except Exception as e:
    print('File not found!', e)
    quit()

print(bigsender, bigcount)

# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
# the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
# second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 Once you have accumulated the
# counts for each hour, print out the counts, sorted by hour as shown below.
file_name = input('Enter file name: ')

if len(file_name) < 0:
    file_name = 'mbox-short.txt'

file_handler = open(file_name)
counts = dict()
lists = list()

# Loop through the file
for line in file_handler:
    # Check if line starts with From
    if line.startswith('From '):
        # Split the words in line
        line_split = line.split()
        # Get the time
        time = line_split[5]
        # Split the time
        time_split = time.split(':')
        # Get the hour
        hour = time_split[0]

        # Put it into a dictionary
        counts[hour] = counts.get(hour, 0) + 1

# Put the items from dictionary to list
for h, c in counts.items():
    lists.append((h, c))

# Sort then print
for h, c in sorted(lists):
    print(h, c)
