
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(100)
);

INSERT INTO employees (id, name, age, department) VALUES (1, 'John Doe', 30, 'HR');
INSERT INTO employees (id, name, age, department) VALUES (2, 'Jane Smith', 35, 'Engineering');
INSERT INTO employees (id, name, age, department) VALUES (3, 'Alice Johnson', 28, 'Marketing');

SELECT * FROM employees;

UPDATE employees SET age = 31 WHERE id = 1;

