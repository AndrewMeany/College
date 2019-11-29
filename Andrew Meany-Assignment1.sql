# Andrew Meany 118755539
# CS2208 Assignment 1

# NOTE: had to re-type all the code on 28/11/19 so I am hoping (some of) it works

# 1
CREATE TABLE Employee (
eid INT(4) UNSIGNED AUTO_INCREMENT,
ename VARCHAR(10) NOT NULL,
age INT(2) NOT NULL,
salary INT(6) NOT NULL, 
PRIMARY KEY (eid),
CHECK (salary >= 200) # 3
);

CREATE TABLE Supervisor (
eid INT(4) UNSIGNED AUTO_INCREMENT,
supervisor_id INT(3) UNSIGNED NOT NULL,
did INT(2) UNSIGNED NOT NULL,
FOREIGN KEY (eid) REFERENCES Employee(eid),
FOREIGN KEY (did) REFERENCES Department(did)
);

CREATE TABLE Works (
eid INT(4) UNSIGNED AUTO_INCREMENT,
did INT(2) UNSIGNED NOT NULL,
pct_time INT(2) UNSIGNED NOT NULL,
rating INT(2) UNSIGNED NOT NULL,
PRIMARY KEY (eid, did),
CHECK (pct_time <= 100), # 7
CHECK ((rating >=0) AND (rating <= 10)) # 5
);

CREATE TABLE Department (
did INT(2) UNSIGNED NOT NULL,
budget INT(6) UNSIGNED,
PRIMARY KEY (did)
);

# 4
delimiter //
CREATE TRIGGER start_rating
BEFORE INSERT ON Employee
FOR EACH ROW 
BEGIN
    IF ((new.rating < 1) OR (new.rating > 3)) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = "Error: Start ratings must be between 1 and 3.";
    END IF;
END; //
delimiter ;

# 2
INSERT INTO Employee (ename, age, salary)
VALUES
    ("Alex", 45, 2000),
    ("Peter", 20, 1500),
    ("John", 28, 1700),
    ("Barry", 25, 700),
    ("Rachel", 22, 500),
    ("Ross", 20, 1000);

INSERT INTO Supervisor (eid, supervisor_id, did)
VALUES
    (1, 1, 1),
    (2, 2, 1),
    (3, 3, 1);

INSERT INTO Works (eid, pct_time, rating)
VALUES
    (1, 100, 1),
    (2, 10, 2),
    (3, 20 ,1),
    (4, 25, 2),
    (5, 100, 1),
    (6, 45, 2);

INSERT INTO Department (did, budget)
VALUES
    (1, 10000);

# 9
delimiter //
CREATE TRIGGER start_rating
AFTER UPDATE ON Works
FOR EACH ROW 
BEGIN
    IF (new.rating >= 1) THEN
        UPDATE Employee SET new.salary = old.salary * 1.10
    END IF;
END; //
delimiter ;

# 10
CREATE VIEW [MANAGER_SALARY] AS
SELECT ename, salary
FROM Employee
WHERE FROM;

# 11
delimiter //
CREATE TRIGGER lowest_ranking
FOR EACH ROW IN Employee
BEGIN
    FOR (MIN(rating) FROM Works)
    END IF;
END; //
delimiter ;

# 12
CREATE VIEW (MINIMUM_PCT_TIME) AS
SELECT ename FROM Employee AND pct_time FROM Works
WHERE pct_time = (SELECT MIN(pct_time) FROM Works);