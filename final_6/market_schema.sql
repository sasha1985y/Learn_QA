-- Создание схемы
CREATE SCHEMA market AUTHORIZATION postgres;

-- Создание таблицы Authors
CREATE TABLE market.Authors (
    ID SERIAL PRIMARY KEY,
    AuthorName VARCHAR(50) NOT NULL UNIQUE
);

-- Создание таблицы Books
CREATE TABLE market.Books (
    ID SERIAL PRIMARY KEY,
    BookName VARCHAR(50) NOT NULL,
    YearOfRelease NUMERIC(5) NOT NULL,
    AuthorID INTEGER NOT NULL,
    CONSTRAINT fk_Books_Authors
        FOREIGN KEY (AuthorID)
            REFERENCES market.Authors (ID)
);

-- Заполнение таблицы Authors
INSERT INTO market.Authors (AuthorName) VALUES
('Фрукты'),
('Мясо'),
('Рыба'),
('Овощи'),
('Выпечка');

-- Заполнение таблицы Books
INSERT INTO market.Books (BookName, YearOfRelease, AuthorID) VALUES
('Охлаждённый окорок', 160, 2),
('Пончики со сгущёнкой', 98, 5),
('Филе горбуши охлаждённое', 1260, 3),
('Морковь мытая', 46, 4),
('Лук репчатый', 78, 4),
('Яблоки Голден', 189, 1),
('Фарш домашний свино-говяжий', 550, 2),
('Мини-пицца', 45, 5),
('Картофель Белорусский', 145, 4),
('Скумбрия заморозка', 260, 3);
