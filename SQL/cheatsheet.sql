-- SQL
-- Create Table
CREATE TABLE Users(
	name VARCHAR(128),
	email VARCHAR(128)
)

-- Inset
INSERT INTO Users (name, email) VALUES ('Ancient', 'ancientfahad@gmail.com')

-- Delete
DELETE FROM Users WHERE email = 'test@test.com'

-- Update
UPDATE Users SET name = 'Fahad Chowdhury' WHERE email = 'fchowdhury137@gmail.com'

-- Select
SELECT * FROM Users WHERE email = 'anannya1927@gmail.com'
SELECT * FROM Users ORDER BY email
SELECT * FROM Users ORDER BY name
SELECT Album.title, Artist.name FROM Album JOIN Artist ON Album.artist_id = Artist.id ;
SELECT Track.title, Genre.name FROM Track JOIN Genre ON Track.genre_id = Genre.id ;

-- Foreign Key
CREATE TABLE "Track" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"title"	TEXT,
	"album_id"	INTEGER,
	"genre_id"	INTEGER,
	"len"	INTEGER,
	"rating"	INTEGER,
	"count"	INTEGER,
	FOREIGN KEY ("album_id") REFERENCES Album ("id"),
	FOREIGN KEY ("genre_id") REFERENCES Genre ("id")
);

SELECT Track.title AS Track_Title, Artist.name AS Artist_Name, Album.title AS Album_Title, Genre.name AS Genre_Name
FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id = Genre.id AND Track.album_id = Album.id AND Album.artist_id = Artist.id
