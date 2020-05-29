import json

file_location = r'C:\Users\fchow\OneDrive\Documents\GitHub\Practice\practice.json'

def open_file():
    try:
        global file_location
        file_handler = open(file_location)
        read_file(file_handler)

    except Exception as e:
        print('File not found', e)


def read_file(file_handler):
    try:
        infos = json.loads(file_handler.read())
        print(infos)

        print('----------')
        for info in infos:

            print('name', info['name'])
            print('call_status', info['call_status'])
            print('relation', info['relation'])
            print('----------')

        file_handler.close()
        write_file(infos)


    except Exception as e:
        print(e)

def write_file(infos):
    try:
        print(infos)

        infos[0]["name"] = "test 1"
        infos[0]["call_status"] = "N"
        infos[0]["relation"] = "friend"

        file_handler = open(file_location, "w+")
        file_handler.write(json.dumps(infos))

        print('----------')
        for info in infos:
            print('name', info['name'])
            print('call_status', info['call_status'])
            print('relation', info['relation'])
            print('----------')

        file_handler.close()

    except Exception as e:
        print(e)


open_file()
