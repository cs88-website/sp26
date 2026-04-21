PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE sales(Cashier,id, cone_id int);
INSERT INTO sales VALUES('Baskin',1,2);
INSERT INTO sales VALUES('Baskin',3,1);
INSERT INTO sales VALUES('Baskin',4,2);
INSERT INTO sales VALUES('Robin',2,3);
INSERT INTO sales VALUES('Robin',5,2);
INSERT INTO sales VALUES('Robin',6,1);

CREATE TABLE cones (Id INT, Flavor TEXT, Color TEXT, Price REAL);
INSERT INTO cones VALUES(1,'strawberry','pink',4.0);
INSERT INTO cones VALUES(2,'chocolate','light brown',3.5);
INSERT INTO cones VALUES(3,'chocolate','dark brown',5.5);
INSERT INTO cones VALUES(4,'strawberry','pink',5.5);
INSERT INTO cones VALUES(5,'bubblegum','pink',3.5);
INSERT INTO cones VALUES(6,'chocolate','dark brown',5.5);
INSERT INTO cones VALUES(7,'vanilla','white',5.0);
COMMIT;
