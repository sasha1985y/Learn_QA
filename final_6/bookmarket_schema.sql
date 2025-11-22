-- Создание схемы
CREATE SCHEMA bookmarket AUTHORIZATION postgres;

-- Создание таблицы Authors
CREATE TABLE
    bookmarket.Authors (
        ID SERIAL PRIMARY KEY,
        AuthorName VARCHAR(50) NOT NULL UNIQUE
    );

-- Создание таблицы Books
CREATE TABLE
    bookmarket.Books (
        ID SERIAL PRIMARY KEY,
        BookName VARCHAR(50) NOT NULL,
        YearOfRelease NUMERIC(5) NOT NULL,
        AuthorID INTEGER NOT NULL,
        CONSTRAINT fk_Books_Authors FOREIGN KEY (AuthorID) REFERENCES bookmarket.Authors (ID)
    );

-- Добавление авторов
INSERT INTO
    bookmarket.Authors (AuthorName)
VALUES
    ('Лев Толстой'),
    ('Федор Достоевский'),
    ('Антон Чехов'),
    ('Александр Пушкин'),
    ('Михаил Булгаков');

-- Добавление книг
INSERT INTO
    bookmarket.Books (BookName, YearOfRelease, AuthorID)
VALUES
    ('Война и мир', 1869, 1),
    ('Преступление и наказание', 1866, 2),
    ('Три сестры', 1901, 3),
    ('Евгений Онегин', 1833, 4),
    ('Мастер и Маргарита', 1967, 5),
    ('Кавказский пленник', 1821, 4),
    ('Полтава', 1829, 4),
    ('Человек в футляре', 1898, 3),
    ('Печенег', 1897, 3),
    ('Ионыч', 1898, 3);

SELECT
    *
FROM
    bookmarket.Books
WHERE
    AuthorID = (
        SELECT
            ID
        FROM
            bookmarket.Authors
        WHERE
            AuthorName = 'Лев Толстой'
    );

SELECT
    a.AuthorName,
    COUNT(b.ID) AS BookCount
FROM
    bookmarket.Authors a
    LEFT JOIN bookmarket.Books b ON a.ID = b.AuthorID
GROUP BY
    a.AuthorName;

SELECT * FROM bookmarket.Books WHERE BookName LIKE 'П%';

SELECT * FROM bookmarket.Books ORDER BY YearOfRelease DESC;

