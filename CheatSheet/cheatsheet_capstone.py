# The code that I was not able to complete during my interview

number_list = [10, 14, 77, 103, 0, -5]
lowest = None
highest = None

for number in number_list:
    if lowest == None:
        lowest = number
    elif lowest > number:
        lowest = number

    if highest == None:
        highest = number
    elif  highest < number:
        highest = number

print(lowest, highest)
