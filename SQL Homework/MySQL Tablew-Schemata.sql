CREATE TABLE `departments` (
    `dept_no` VARCHAR(4)  NOT NULL ,
    `dept_name` VARCHAR(30)  NOT NULL ,
    PRIMARY KEY (
        `dept_no`
    )
);

CREATE TABLE `dept_emp` (
    `emp_no` INT  NOT NULL ,
    `dept_no` VARCHAR(4)  NOT NULL ,
    `from_date` DATE  NOT NULL ,
    `to_date` DATE  NOT NULL 
);

CREATE TABLE `dept_manager` (
    `dept_no` VARCHAR(4)  NOT NULL ,
    `emp_no` INT  NOT NULL ,
    `from_date` DATE  NOT NULL ,
    `to_date` DATE  NOT NULL 
);

CREATE TABLE `employees` (
    `emp_no` INT  NOT NULL ,
    `birth_date` DATE  NOT NULL ,
    `first_name` VARCHAR(30)  NOT NULL ,
    `last_name` VARCHAR(30)  NOT NULL ,
    `gender` VARCHAR(30)  NOT NULL ,
    `hire_date` DATE  NOT NULL ,
    PRIMARY KEY (
        `emp_no`
    )
);

CREATE TABLE `salaries` (
    `emp_no` INT  NOT NULL ,
    `salary` INT  NOT NULL ,
    `from_date` DATE  NOT NULL ,
    `to_date` DATE  NOT NULL 
);

CREATE TABLE `titles` (
    `emp_no` INT  NOT NULL ,
    `title` VARCHAR(30)  NOT NULL ,
    `from_date` DATE  NOT NULL ,
    `to_date` DATE  NOT NULL 
);

ALTER TABLE `dept_emp` ADD CONSTRAINT `fk_dept_emp_emp_no` FOREIGN KEY(`emp_no`)
REFERENCES `employees` (`emp_no`);

ALTER TABLE `dept_emp` ADD CONSTRAINT `fk_dept_emp_dept_no` FOREIGN KEY(`dept_no`)
REFERENCES `departments` (`dept_no`);

ALTER TABLE `dept_manager` ADD CONSTRAINT `fk_dept_manager_dept_no` FOREIGN KEY(`dept_no`)
REFERENCES `departments` (`dept_no`);

ALTER TABLE `dept_manager` ADD CONSTRAINT `fk_dept_manager_emp_no` FOREIGN KEY(`emp_no`)
REFERENCES `employees` (`emp_no`);

ALTER TABLE `salaries` ADD CONSTRAINT `fk_salaries_emp_no` FOREIGN KEY(`emp_no`)
REFERENCES `employees` (`emp_no`);

ALTER TABLE `titles` ADD CONSTRAINT `fk_titles_emp_no` FOREIGN KEY(`emp_no`)
REFERENCES `employees` (`emp_no`);

select * from titles;

-- List details of each employee: employee number, last name, first name, gender, and salary.
SELECT employees.emp_no, employees.last_name, employees.first_name, employees.gender, salaries.salary FROM employees
JOIN salaries ON employees.emp_no = salaries.emp_no;

-- List employees who were hired in 1986.
SELECT first_name, last_name, hire_date FROM employees
WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31';

-- List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
SELECT departments.dept_no, departments.dept_name, dept_manager.emp_no, employees.last_name, employees.first_name, dept_manager.from_date, dept_manager.to_date FROM departments
JOIN dept_manager ON departments.dept_no = dept_manager.dept_no
JOIN employees ON dept_manager.emp_no = employees.emp_no;

--  List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT dept_emp.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM dept_emp
JOIN employees
ON dept_emp.emp_no = employees.emp_no
JOIN departments
ON dept_emp.dept_no = departments.dept_no;

-- List all employees whose first name is "Hercules" and last names begin with "B."
SELECT first_name, last_name
FROM employees
WHERE first_name = 'Hercules'
AND last_name LIKE 'B%';

-- List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT dept_emp.emp_no, employees.last_name, employees.first_name, departments.dept_name FROM dept_emp
JOIN employees ON dept_emp.emp_no = employees.emp_no
JOIN departments ON dept_emp.dept_no = departments.dept_no
WHERE departments.dept_name = 'Sales';

-- List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT dept_emp.emp_no, employees.last_name, employees.first_name, departments.dept_name FROM dept_emp
JOIN employees ON dept_emp.emp_no = employees.emp_no
JOIN departments ON dept_emp.dept_no = departments.dept_no
WHERE departments.dept_name = 'Development' OR departments.dept_name = 'Sales';

-- In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT last_name,
COUNT(last_name) AS "frequency" FROM employees
GROUP BY last_name ORDER BY COUNT(last_name) DESC;