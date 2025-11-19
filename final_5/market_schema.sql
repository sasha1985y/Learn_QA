-- Создание схемы
CREATE SCHEMA market AUTHORIZATION postgres;

-- Создание таблицы Categories
CREATE TABLE market.Categories (
    ID SERIAL PRIMARY KEY,
    CategorieName VARCHAR(50) NOT NULL UNIQUE
);

-- Создание таблицы Goods
CREATE TABLE market.Goods (
    ID SERIAL PRIMARY KEY,
    GoodName VARCHAR(50) NOT NULL,
    Price NUMERIC(5) NOT NULL,
    CategorieID INTEGER NOT NULL,
    CONSTRAINT fk_Goods_Categories
        FOREIGN KEY (CategorieID)
            REFERENCES market.Categories (ID)
);

-- Заполнение таблицы Categories
INSERT INTO market.Categories (CategorieName) VALUES
('Фрукты'),
('Мясо'),
('Рыба'),
('Овощи'),
('Выпечка');

-- Заполнение таблицы Goods
INSERT INTO market.Goods (GoodName, Price, CategorieID) VALUES
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
