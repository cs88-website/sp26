CREATE TABLE finals (hall TEXT, course TEXT);

INSERT INTO finals VALUES
('RSF', '61A'),
('Wheeler', '61A'),
('Pimentel', '61A'),
('Li Ka Shing', '61A'),
('Stanley', '61A'),
('RSF', '61B'),
('Wheeler', '61B'),
('Morgan', '61B'),
('Wheeler', '61C'),
('Pimentel', '61C'),
('Soda 310', '61C'),
('Soda 306', '10'),
('RSF', '70');

CREATE TABLE sizes (room TEXT, seats INTEGER);

INSERT INTO sizes VALUES
('RSF', 900),
('Wheeler', 700),
('Pimentel', 500),
('Li Ka Shing', 300),
('Stanley', 300),
('Morgan', 100),
('Soda 306', 80),
('Soda 310', 40),
('Soda 320', 30);


CREATE TABLE big AS
  SELECT course
  FROM finals, sizes
  WHERE hall = room
  GROUP BY course
  HAVING SUM(seats) >= 1000;


CREATE TABLE remaining AS
  SELECT course, SUM(seats) - MAX(seats) AS remaining
  FROM finals, sizes
  WHERE hall = room
  GROUP BY course;


CREATE TABLE sharing AS
  SELECT a.course, COUNT(DISTINCT a.hall) AS shared
  FROM finals AS a, finals AS b
  WHERE a.hall = b.hall AND a.course != b.course
  GROUP BY a.course;

