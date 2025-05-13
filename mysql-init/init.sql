USE mbti;

CREATE TABLE mbti_labels (
  id BIGINT PRIMARY KEY,
  mbti_personality VARCHAR(10) NOT NULL,
  pers_id INT NOT NULL
);

LOAD DATA INFILE '/data/mbti_labels.csv'
INTO TABLE mbti_labels
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
  id,
  mbti_personality,
  pers_id
);