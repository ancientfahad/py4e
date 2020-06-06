import json, sys, time, re, shutil, os

# file location windows
# file_location = r'C:\Users\fchow\OneDrive\Documents\GitHub\Practice\'

# file location mac
folder_location = os.getcwd()
file_location = None
file_name = None
json_file = None
json_data = None


def format_data(_name, _call_status, _relation):
    json_format = {
    "name" : _name,
    "call_status" : _call_status,
    "relation" : _relation
    }

    return json_format


def loading(text, delay):
    for characters in text:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(delay)
    print


def main():
    global file_location, folder_location, file_name, json_file, json_data

    try:
        while True:
            choice = int(input('1. Read data\n2. Add data\n3. Update data\n4. Upload data\n5. Exit\nEnter your choice : '))

            if choice not in range(1, 6):
                print('\nInvalid answer!\n')
            else:
                if choice == 1:
                    json_data = open_fileR()
                    print_data(json_data)
                elif choice == 2:
                    add_data()
                elif choice == 3:
                    update_data()
                elif choice == 4:
                    pass
                else:
                    print()
                    quit()
    except Exception as e:
        print('Error _main!', e)


def open_fileR():
    global file_location, folder_location, file_name, json_file, json_data

    try:
        file_name = 'practice.json'
        file_location = folder_location + ('/' + file_name)

        loading(('\nSearching for ' + file_name + ' .....'), 0.04)
        json_file = open(file_location, "r")
        loading('\nSearching complete .....', 0.04)

        print('\n\nFile found in', file_location)

        if os.path.getsize('practice.json') == 0:
            print('\nFile is empty!\n')
            return None
        else:
            json_data = json.loads(json_file.read())
            return(json_data)

    except Exception as e:
        print('\n\nFile not found!\n', e)
        print()


def open_fileW():
    global file_location, folder_location, file_name, json_file, json_data

    try:
        file_name = 'practice.json'
        file_location = folder_location + ('/' + file_name)
        json_file = open(file_location, "r")
        json_data = json.loads(json_file.read())
        json_file.close()

        return json_data

    except Exception as e:
        print('Error _open_fileW!', e)
        print()


def update_file(json_file, json_datas):
    print()
    print(json.dumps(json_data,indent = 4))
    print()

    loading(('\nUpdating data .....'), 0.04)
    json_file.seek(0)
    json_file.write(json.dumps(json_data))
    loading('\nUpdating complete .....\n\n', 0.04)


def print_data(json_data):
    print()
    print(json.dumps(json_data,indent = 4))

    if len(json_data['call_details']) < 1:
        print('\nNo data found!\n')
    else:
        loading('\nRetrieving data .....\n', 0.04)

        for data in json_data['call_details']:
            print('name         :', data['name'])
            print('call_status  :', data['call_status'])
            print('relation     :', data['relation'])
            print()


def add_data():
    global file_location, folder_location, file_name, json_file, json_data

    json_data = open_fileW()
    json_file = open(file_location, "w")

    _name = input('\nEnter name: ')
    _call_status = input('Enter call status: ')
    _relation = input('Enter relation: ')

    json_data['call_details'].append(format_data(_name, _call_status, _relation))

    print(json.dumps(json_data,indent = 4))
    loading(('\nAdding data .....'), 0.04)
    json_file.seek(0)
    json_file.write(json.dumps(json_data))
    loading('\nAdding complete .....\n\n', 0.04)


def update_data():
    global file_location, folder_location, file_name, json_file, json_data

    json_data = open_fileW()
    json_file = open(file_location, "w")

    print()
    print(json.dumps(json_data,indent = 4))
    print()

    user_choice = input('Do you want to update all users data or single user data? [A/S]: ').upper()

    if user_choice == 'A':
        _call_status = input('\nEnter call status for all user [Y/N]: ').upper()

        for data in json_data['call_details']:
            data['call_status'] = _call_status

        update_file(json_file, json_data)
    else:
        selected_user = input('\nType user name: ')

        for data in json_data['call_details']:
            if data['name'] == selected_user:

                print()
                print('User selected: ', data['name'])
                print()

                # _name = input('Enter name: ')
                _call_status = input('Enter call status: ')
                # _relation = input('Enter relation: ')

                # data['name'] = _name
                data['call_status'] = _call_status
                # data['relation'] = _relation

                update_file(json_file, json_data)

                break


def upload_data():
    pass


main()

# https://stackoverflow.com/questions/36606930/delete-an-element-in-a-json-object
