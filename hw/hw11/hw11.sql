CREATE TABLE parents (parent TEXT, child TEXT);

INSERT INTO parents VALUES
  ('ace', 'bella'),
  ('ace', 'charlie'),
  ('daisy', 'hank'),
  ('finn', 'ace'),
  ('finn', 'daisy'),
  ('finn', 'ginger'),
  ('ellie', 'finn');

CREATE TABLE dogs (name TEXT, fur TEXT, height INTEGER);

INSERT INTO dogs VALUES
  ('ace',     'long',  26),
  ('bella',   'short', 52),
  ('charlie', 'long',  47),
  ('daisy',   'long',  46),
  ('ellie',   'short', 35),
  ('finn',    'curly', 32),
  ('ginger',  'short', 28),
  ('hank',    'curly', 31);

CREATE TABLE sizes (size TEXT, min INTEGER, max INTEGER);

INSERT INTO sizes VALUES
  ('toy',      24, 28),
  ('mini',     28, 35),
  ('medium',   35, 45),
  ('standard', 45, 60);


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE turkeys AS
  SELECT 18 AS age, 16.5 AS weight, "Pecan" AS name UNION
  SELECT 30       , 22.1          , "Waddle"        UNION
  SELECT 12       , 17.3          , "Bud"           UNION
  SELECT 14       , 15.3          , "Bird"          UNION
  SELECT 30       , 26.8          , "Tom"           UNION
  SELECT 26       , 18.4          , "Flappy"        UNION
  SELECT 18       , 19.3          , "Pumpkin";

CREATE TABLE big AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

CREATE TABLE growing AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

