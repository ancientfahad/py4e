# import sqlite3
#
# connection = sqlite3.connect('Counts.sqlite')
# cur = connection.cursor()
#
# cur.execute('DROP TABLE IF EXISTS Counts')
# cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
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
#         email_split = email.split('@')
#         domain = email_split[1]
#
#         _domain = {'domain': domain}
#
#         cur.execute('SELECT count FROM Counts WHERE org = :domain', _domain)
#
#         row = cur.fetchone()
#         if row is None:
#             cur.execute('INSERT INTO Counts (org, count) VALUES (:domain, 1)', _domain)
#             print(_domain)
#         else:
#             cur.execute('UPDATE Counts SET count = count + 1 WHERE org = :domain', _domain)
#
#         connection.commit()
#
# sql_string = 'SELECT * FROM Counts ORDER BY count DESC'
#
# for row in cur.execute(sql_string):
#     print(str(row[0]), row[1])
#
# cur.close()

# import xml.etree.ElementTree as ET
# import sqlite3
#
# conn = sqlite3.connect('trackdb.sqlite')
# cur = conn.cursor()
#
#
# def retrieve_data():
#     sql_string = '''
#     SELECT Track.title, Artist.name, Album.title, Genre.name
#     FROM Track JOIN Genre JOIN Album JOIN Artist
#         ON Track.genre_id = Genre.ID
#             AND Track.album_id = Album.id
#             AND Album.artist_id = Artist.id
#         ORDER BY Artist.name LIMIT 3
#     '''
#     print('Track                                    Artist          Album           Genre')
#     for row in cur.execute(sql_string):
#         print(row[0], row[1], row[2], row[3])
#
#
# def insert_data():
#     # Make some fresh tables using executescript()
#     cur.executescript('''
#     DROP TABLE IF EXISTS Artist;
#     DROP TABLE IF EXISTS Album;
#     DROP TABLE IF EXISTS Track;
#     DROP TABLE IF EXISTS Genre;
#
#     CREATE TABLE Artist (
#         id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#         name    TEXT UNIQUE
#     );
#
#     CREATE TABLE Album (
#         id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#         artist_id  INTEGER,
#         title   TEXT UNIQUE
#     );
#
#     CREATE TABLE Genre (
#         id  INTEGER NOT NULL PRIMARY KEY
#             AUTOINCREMENT UNIQUE,
#         name TEXT  UNIQUE
#     );
#
#     CREATE TABLE Track (
#         id  INTEGER NOT NULL PRIMARY KEY
#             AUTOINCREMENT UNIQUE,
#         title TEXT  UNIQUE,
#         album_id  INTEGER,
#         genre_id INTEGER,
#         len INTEGER, rating INTEGER, count INTEGER
#     );
#     ''')
#
#     fname = input('Enter file name: ')
#     if ( len(fname) < 1 ) : fname = 'Library.xml'
#
#     # <key>Track ID</key><integer>369</integer>
#     # <key>Name</key><string>Another One Bites The Dust</string>
#     # <key>Artist</key><string>Queen</string>
#     def lookup(d, key):
#         found = False
#         for child in d:
#             if found : return child.text
#             if child.tag == 'key' and child.text == key :
#                 found = True
#         return None
#
#     stuff = ET.parse(fname)
#     all = stuff.findall('dict/dict/dict')
#     print('Dict count:', len(all))
#     for entry in all:
#         if ( lookup(entry, 'Track ID') is None ) : continue
#
#         name = lookup(entry, 'Name')
#         artist = lookup(entry, 'Artist')
#         album = lookup(entry, 'Album')
#         count = lookup(entry, 'Play Count')
#         rating = lookup(entry, 'Rating')
#         length = lookup(entry, 'Total Time')
#         genre = lookup(entry, 'Genre')
#
#         if name is None or artist is None or album is None or genre is None :
#             continue
#
#         # Artist
#         cur.execute('''INSERT OR IGNORE INTO Artist (name)
#             VALUES ( ? )''', ( artist, ) )
#         # Artist ID
#         cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
#         artist_id = cur.fetchone()[0]
#
#         # Album
#         cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
#             VALUES ( ?, ? )''', ( album, artist_id ) )
#         # Album ID
#         cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
#         album_id = cur.fetchone()[0]
#
#         # Genre
#         cur.execute('''INSERT OR IGNORE INTO Genre (name)
#             VALUES ( ? )''', ( genre, ) )
#         # Genre ID
#
#         cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
#         genre_id = cur.fetchone()[0]
#
#
#         cur.execute('''INSERT OR REPLACE INTO Track
#             (title, album_id, genre_id, len, rating, count)
#             VALUES ( ?, ?, ?, ?, ?, ? )''',
#             ( name, album_id, genre_id, length, rating, count ) )
#
#         conn.commit()
#
# insert_data()
# retrieve_data()

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0];
    title = entry[1];
    role = entry[2];

    print((name, title, role))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

    conn.commit()
