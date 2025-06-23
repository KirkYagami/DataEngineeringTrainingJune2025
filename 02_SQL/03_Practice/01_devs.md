# Schema
### 1. `programmers` Table
```sql
CREATE TABLE programmers (
    Programmer_Name VARCHAR(100) PRIMARY KEY,
    DOB DATE,
    DOJ DATE,
    GENDER CHAR(1),
    Primary_Language VARCHAR(100),
    Secondary_Language VARCHAR(100),
    Salary DECIMAL(10, 2)
);

INSERT INTO programmers (Programmer_Name, DOB, DOJ, GENDER, Primary_Language, Secondary_Language, Salary) VALUES
('Tony Stark', '1970-05-29', '1990-05-11', 'M', 'Python', 'JavaScript', 15000),
('Peter Parker', '2001-08-10', '2018-06-15', 'M', 'JavaScript', 'Python', 12000),
('Thomas Shelby', '1980-11-20', '1999-09-12', 'M', 'Python', 'R', 16000),
('John Wick', '1964-09-18', '1987-10-05', 'M', 'Java', 'C++', 18000),
('Bruce Wayne', '1933-02-19', '1950-06-11', 'M', 'C#', 'Java', 14000),
('Clark Kent', '1938-06-18', '1956-07-01', 'M', 'Java', 'Python', 13500),
('Diana Prince', '1919-08-19', '1945-07-01', 'F', 'Ruby', 'Python', 17500),
('Natasha Romanoff', '1984-11-22', '2000-05-30', 'F', 'Go', 'Rust', 14500),
('Steve Rogers', '1918-07-04', '1943-04-10', 'M', 'C++', 'C', 15500),
('Bruce Banner', '1969-12-18', '1989-07-20', 'M', 'Python', 'JavaScript', 14200),
('Wanda Maximoff', '1989-02-13', '2005-09-12', 'F', 'Swift', 'Kotlin', 14800),
('Stephen Strange', '1936-11-01', '1965-10-15', 'M', 'Fortran', 'Lisp', 15200),
('Thor Odinson', '1900-07-20', '2002-06-01', 'M', 'R', 'Julia', 16200);
```

### 2. `studies` Table
```sql
CREATE TABLE studies (
    Programmer_Name VARCHAR(100),
    Institute VARCHAR(100),
    Course VARCHAR(100),
    Course_Fee DECIMAL(10, 2),
    FOREIGN KEY (Programmer_Name) REFERENCES programmers(Programmer_Name)
);

INSERT INTO studies (Programmer_Name, Institute, Course, Course_Fee) VALUES
('Tony Stark', 'MIT', 'Computer Science', 4500),
('Peter Parker', 'Stanford', 'Data Science', 7200),
('Thomas Shelby', 'Columbia', 'Artificial Intelligence', 22000),
('John Wick', 'Oxford', 'Machine Learning', 5000),
('Bruce Wayne', 'MIT', 'Cybersecurity', 4500),
('Clark Kent', 'Stanford', 'Robotics', 6200),
('Diana Prince', 'Oxford', 'Quantum Computing', 5200),
('Natasha Romanoff', 'Cambridge', 'Bioinformatics', 14000),
('Steve Rogers', 'MIT', 'Software Engineering', 4500),
('Bruce Banner', 'Columbia', 'Cloud Computing', 11000),
('Wanda Maximoff', 'Cambridge', 'Data Analytics', 6000),
('Stephen Strange', 'MIT', 'Quantum Mechanics', 5000),
('Thor Odinson', 'Columbia', 'Data Science', 48000);
```

### 3. `software` Table
```sql
CREATE TABLE software (
    Programmer_Name VARCHAR(100),
    Software_Name VARCHAR(100),
    Developed_In VARCHAR(100),
    Software_Cost DECIMAL(10, 2),
    Development_Cost DECIMAL(10, 2),
    Sold INT,
    FOREIGN KEY (Programmer_Name) REFERENCES programmers(Programmer_Name)
);

INSERT INTO software (Programmer_Name, Software_Name, Developed_In, Software_Cost, Development_Cost, Sold) VALUES
('Tony Stark', 'Jarvis', 'Python', 15000, 30000, 150),
('Peter Parker', 'Spider Tracker', 'JavaScript', 8000, 20000, 85),
('Thomas Shelby', 'AI Advisor', 'Python', 20000, 50000, 70),
('John Wick', 'Assassin App', 'Java', 18000, 35000, 60),
('Bruce Wayne', 'Bat Computer', 'C#', 25000, 60000, 90),
('Clark Kent', 'Super Scanner', 'Java', 12000, 30000, 55),
('Diana Prince', 'Lasso of Truth', 'Ruby', 10000, 25000, 45),
('Natasha Romanoff', 'Black Widow Network', 'Go', 14000, 35000, 75),
('Steve Rogers', 'Shield Defense', 'C++', 16000, 40000, 80),
('Bruce Banner', 'Hulk Smash App', 'Python', 14000, 30000, 65),
('Wanda Maximoff', 'Hex Control', 'Swift', 12000, 28000, 50),
('Stephen Strange', 'Time Manipulator', 'Fortran', 16000, 45000, 70),
('Thor Odinson', 'Mjolnir Control', 'R', 18000, 50000, 100);
```

---


# Practice Questions

**Basic Queries (SELECT, WHERE, ORDER BY):**

1. List the names and dates of birth of all programmers.
2. Display the names of programmers whose primary language is 'Python'.
3. Show the names of programmers who joined the company after the year 2000.
4. List the names and salaries of all female programmers.
5. Display the names of programmers sorted by their date of birth in ascending order.
6. Find the names of programmers whose secondary language is 'Java'.
7. Show the details of programmers who earn a salary greater than $15,000.
8. List the names of programmers whose primary language is 'C++' and who were born before 1970.
9. Display the software names developed in 'Java'.
10. List the courses studied at 'MIT'.

**Aggregate Functions (COUNT, AVG, MIN, MAX, SUM):**

11. What is the average salary of all programmers?
12. How many programmers know 'Python' as their primary language?
13. What is the highest salary paid to a programmer?
14. What is the total development cost of all software?
15. What is the minimum course fee paid by a programmer?
16. How many software packages were sold in total?
17. What is the average cost of a course at 'Columbia'?
18. How many male programmers are in the database?
19. What is the sum of the software costs of packages developed in 'R'?
20. What is the maximum development cost for a package?

**Grouping and Filtering (GROUP BY, HAVING):**

21. Display the average salary for each primary language.
22. How many software packages were developed by each programmer?
23. Show the number of programmers for each gender.
24. List the institutes and the number of courses offered by each.
25. Find the primary languages where the average salary is greater than $15,000.
26. Display the total sales for each software developer.
27. List the software languages and the number of software packages developed in each.
28. Show the average course fee for each institute.
29. Find the programmers who have developed more than one software package.
30. Display the number of courses for each institute, but only for institutes with more than two courses.

**Joins (INNER JOIN, LEFT JOIN, RIGHT JOIN):**

31. Display the names of programmers and the software they developed.
32. List the programmers and the institutes where they studied.
33. Show the names of programmers and their course fees.
34. Find the software names and the institutes where the developers studied.
35. Display the programmers and the courses they studied, including those who didn't study any course.
36. Show the names of programmers and their software, including those who didn't develop any software.
37. List the institutes and the software developed by their students.
38. Display the programmer names, their primary languages, and the software names developed in those languages.
39. Find the programmer names and the courses they studied, only for courses with fees greater than $5,000.
40. Show the software names and the institute names where the developers studied, only for institutes located at 'MIT'.

**Subqueries and Complex Queries:**

41. Find the programmer who developed the most expensive software.
42. List the programmers who earn more than the average salary of all programmers.
43. Display the software names that have a development cost higher than the average development cost.
44. Find the programmers who studied at the institute with the highest average course fee.
45. List the software names developed by programmers who know 'Python'.
46. Show the programmers who have not developed any software.
47. Find the institute with the most number of students.
48. Display the programmers who earn the highest salary in their primary language category.
49. List the software packages developed by programmers who have studied a course with a fee greater than $10,000.
50. Find the programmers who have developed software in their secondary language.
51. Find the programmers that have the same secondary language.
52. Who is the youngest programmer in the database?
53. Who is the oldest programmer in the database?
54. List the programmers who share the same date of joining.
55. Display the programmers who's software sold more than the average number of sales.
56. Find the programmers who's software cost is higher than their salary.
57. Display the programmers who's software development cost is higher than their salary.
58. List the programmers who have studied the same course.
59. Display the programmers who have developed software that sold less than the average amount.
60. Find the programmers who have developed software that costs less than the average course fee.

**Date and Time Functions:**

61. Display the programmers who were born in the same month as their joining month.
62. How many programmers were born in the 1980s?
63. List the programmers whose birthday is in the current month.
64. Display the programmers who joined on a Monday.
65. Calculate the age of each programmer.
66. Calculate the number of years of experience for each programmer.
67. List the programmers whose birthday is on the 1st of any month.
68. Display the programmers who joined in the first half of the year.
69. List the programmers who were born in a leap year.
70. Display the programmers who have joined in the last 5 years.