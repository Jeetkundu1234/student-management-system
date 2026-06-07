CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50),
    phone VARCHAR(15)
);
USE student_db;

SHOW TABLES;
SELECT * FROM students;