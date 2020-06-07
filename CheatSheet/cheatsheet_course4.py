# sample_list = [108, 105, 115, 116]
# output = ''
#
# for num in sample_list:
#     output = output + chr(num)
#
# print(output)
#
# # Class
# class tryClass:
#     result = 0
#
#     def __init__(self):
#         print('I am constructed')
#
#
#     def _tryFunction(self):
#         self.result = self.result + 1
#         print(self.result)
#
#
#     def __del__(self):
#         print('I am destructed', self.result)
#
#
# _tryClass = tryClass()
# _tryClass._tryFunction()
# _tryClass._tryFunction()
#
# _tryClass = 42
#
# print('_tryClass containts', _tryClass)
#
# class Mathematics:
#     result = 0
#     num = 0
#
#     def __init__(self, num):
#         self.num = num
#         print('I am constructed', self.num)
#
#
#     def _addition(self, num1, num2):
#         self.result = num1 + num2
#         print(self.result)
#
#
#     def _subtraction(self, num1, num2):
#         self.result = num1 - num2
#         print(self.result)
#
#
#     def __del__(self):
#         print('I am destructed', self.result, self.num)
#
#
# class additionalMathematics(Mathematics):
#     additionalResult = 0
#
#
#     def _multiplication(self, num1, num2):
#         self.additionalResult = num1 * num2
#         print(self.additionalResult)
#
#
#     def _division(self, num1, num2):
#         self.additionalResult = num1 / num2
#         print(self.additionalResult)
#
#
# # _mathematics = Mathematics()
# # _mathematics._addition(5, 5)
# # _mathematics._subtraction(5, 5)
#
# _additonalMathematics = additionalMathematics(10)
# _additonalMathematics._addition(5, 5)
# _additonalMathematics._subtraction(5, 5)
# _additonalMathematics._multiplication(5, 5)
# _additonalMathematics._division(5, 5)

# # SQL
# import sqlite3
#
# connection = sqlite3.connect('emaildb.sqlite')
# cur = connection.cursor()
#
# cur.execute('DROP TABLE IF EXISTS Counts')
# cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')
#
# file_name = input('Enter file name: ')
#
# try:
#     file_handler = open(file_name)
# except Exception as e:
#     print('Error while opening file!', e)
#
# for line in file_handler:
#     if line.startswith('From: '):
#         line_split = line.split()
#         email = line_split[1]
#
#         cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
#
#         row = cur.fetchone()
#         if row is None:
#             cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
#         else:
#             cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ? ', (email,))
#
#         connection.commit()
#
# sql_string = 'SELECT * FROM Counts ORDER BY count DESC'
#
# for row in cur.execute(sql_string):
#     print(str(row[0]), row[1])

import sqlite3
from sqlite3 import Error

connection = None
cur = None

def create_connection():
    global connection, cur

    try:
        connection = sqlite3.connect('/Users/u75530/Documents/GitHub/Databases/track_management_test.db')
        cur = connection.cursor()
    except Exception as e:
        print('Unable to create connection with DB!', e)


def insert_Artist(artist_name):
    global connection, cur

    try:
        _artist_name = {'artist_name': artist_name}
        cur.execute('INSERT INTO Artist (name) VALUES (:artist_name)', _artist_name)
        connection.commit()
        cur.close()
        print('insert_Artist successfull!')

    except Exception as e:
        print('insert_Artist unsuccessfull', e)


def insert_Genre(genre_name):
    global connection, cur

    try:
        _genre_name = {'genre_name': genre_name}
        cur.execute('INSERT INTO Genre (name) VALUES (:genre_name)', _genre_name)
        connection.commit()
        cur.close()
        print('insert_Genre successfull!')

    except Exception as e:
        print('insert_Genre unsuccessfull!', e)


def insert_Album(album_title, artist_id):
    global connection, cur

    try:
        param = dict()
        param['album_title'] = album_title
        param['artist_id'] = artist_id

        print(param)
        sql_string = 'INSERT INTO Album (title, artist_id) VALUES(:album_title, :artist_id)'

        cur.execute(sql_string, param)
        connection.commit()
        cur.close()
        print('insert_Album successfull!')

    except Exception as e:
        print('insert_Album unsuccessfull!', e)


def get_artist_id(artist_name):
    global connection, cur

    try:
        _artist_name = {'artist_name': artist_name}

        sql_string = 'SELECT id FROM Artist WHERE name = :artist_name'

        for row in cur.execute(sql_string, _artist_name):
            return int(row[0])

    except Exception as e:
        print('get_artist_id unsuccessfull!', e)


create_connection()

# artist_name = input('Enter artist name: ')
# insert_Artist(artist_name)

# genre_name = input('Enter genre name: ')
# insert_Genre(genre_name)

album_title = input('Enter album name: ')
artist_name = input('Enter artist name: ')

artist_id = get_artist_id(artist_name)

insert_Album(album_title, artist_id)
