-- Создание схемы (если еще не создана)
CREATE SCHEMA IF NOT EXISTS lessons;
GRANT ALL PRIVILEGES ON SCHEMA lessons TO postgres;

-- Таблица групп
CREATE TABLE lessons.Groups (
    ID SERIAL PRIMARY KEY,           -- Уникальный идентификатор группы
    GroupNumber NUMERIC(2) NOT NULL UNIQUE   -- Номер группы (уникален)
);

-- Таблица студентов
CREATE TABLE lessons.Students (
    ID SERIAL PRIMARY KEY,          -- Уникальный идентификатор студента
    StudentName VARCHAR(50) NOT NULL,  -- Имя студента
    GroupID NUMERIC(2) NOT NULL,  -- Уникальный номер группы
    CONSTRAINT fk_Students_Groups FOREIGN KEY (GroupID) REFERENCES lessons.Groups(GroupNumber)
);

-- Функция триггера
CREATE OR REPLACE FUNCTION lessons.update_student_group_number()
RETURNS TRIGGER AS $$
BEGIN
    -- Обновляем только при изменениях номера группы
    IF TG_OP = 'UPDATE' AND NEW.GroupNumber <> OLD.GroupNumber THEN
        -- Для каждого студента, чья текущая группа совпадает с прежним номером группы, обновляем его группу
        UPDATE lessons.Students
        SET GroupNumber = NEW.GroupNumber
        WHERE GroupNumber = OLD.GroupNumber;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Триггер выполняется сразу после обновления группы
CREATE TRIGGER trg_update_group_number
AFTER UPDATE ON lessons.Groups
FOR EACH ROW
EXECUTE FUNCTION lessons.update_student_group_number();

-- Вставляем тестовые данные в таблицу Groups
INSERT INTO lessons.Groups (GroupNumber)
VALUES
    (1),
    (2),
    (3),
    (4),
    (5);

-- Перемещаем студентов внутри одной группы, используя изменение номера группы
INSERT INTO lessons.Students (StudentName, GroupID)
VALUES
    ('Иванов Иван', 1),
    ('Петров Петр', 1),
    ('Сидоров Сидор', 2),
    ('Кузнецов Николай', 2),
    ('Смирнова Анна', 3),
    ('Попова Ольга', 3),
    ('Федоров Алексей', 4),
    ('Морозов Андрей', 4),
    ('Ковалев Сергей', 5),
    ('Лебедева Мария', 5),
    ('Григорьев Артем', 1),
    ('Никитина Светлана', 2),
    ('Соловьев Денис', 3),
    ('Васильева Дарья', 4),
    ('Зайцева Анастасия', 5);

UPDATE lessons.Students SET StudentName = 'Иванова Ирина' WHERE ID = 1;

SELECT * FROM lessons.Students WHERE ID = 1;

SELECT * FROM lessons.Students WHERE GroupID = 1;

SELECT * FROM lessons.Groups;

SELECT * FROM lessons.Students;

UPDATE lessons.Students SET GroupID = 3 WHERE ID IN (2, 3, 4);

SELECT * FROM lessons.Students WHERE ID IN (2, 3, 4);

UPDATE lessons.Groups SET GroupNumber = 10 WHERE ID = 1;

SELECT * FROM lessons.Groups WHERE ID = 1;

UPDATE lessons.Students SET StudentName = 'Василий Сахаров', GroupID = 5 WHERE ID = 5;
   
SELECT * FROM lessons.Students WHERE ID = 5;
   

   

   


   
