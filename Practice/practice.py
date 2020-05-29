import json
import sys
import time
import re

# file location windows
# file_location = r'C:\Users\fchow\OneDrive\Documents\GitHub\Practice\practice.json'

# file location mac
folder_location = '/Users/u75530/Documents/GitHub/Practice/'
file_location = None
file_name = None


def loading(text, delay):
    for characters in text:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(delay)
    print


def open_file():
    try:
        global file_location, folder_location, file_name

        file_name = input('\nEnter file name: ')
        file_location = folder_location + file_name

        loading(('\nSearching for ' + file_name + ' .....'), 0.05)
        file_handler = open(file_location)
        loading('\nSearching complete .....', 0.05)

        print('\n\nFile found in', file_location)

        read_file(file_handler)

    except Exception as e:
        print('\n\nFile not found!', e)
        print()


def read_file(file_handler):
    try:
        infos = json.loads(file_handler.read())

        loading('\nRetrieving data .....\n', 0.05)

        for info in infos['call_details']:
            print('name         :', info['name'])
            print('call_status  :', info['call_status'])
            print('relation     :', info['relation'])
            print()

        file_handler.close()

        write_file(infos)


    except Exception as e:
        print('\n\nFile could not be read!', e)


def write_file(infos):
    try:
        global file_location, folder_location, file_name

        while True:
            choice = input('Do you want to update data? [Y/N] : ')

            if choice == 'Y' or choice == 'N':
                if choice == 'Y':
                    infos['call_details'][0]['name'] = 'test xxx'
                    infos['call_details'][0]['call_status'] = 'N'
                    infos['call_details'][0]['relation'] = 'relative'

                    file_handler = open(file_location, "w+")

                    loading(('\nUpdating ' + file_name + ' .....'), 0.05)
                    file_handler.write(json.dumps(infos))
                    loading('\nUpdating complete .....\n\n', 0.05)

                    for info in infos['call_details']:
                        print('name         :', info['name'])
                        print('call_status  :', info['call_status'])
                        print('relation     :', info['relation'])
                        print()

                    file_handler.close()
                else:
                    print()
                    break

                break
            else:
                print('\nInvalid answer! Enter Y or N\n')

    except Exception as e:
        print('\n\nFile could not be updated!', e)
        print()

open_file()
