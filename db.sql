DROP INDEX IF EXISTS image_upload_datetime_idx;
DROP INDEX IF EXISTS image_name_idx;

DROP TABLE IF EXISTS image;
DROP TABLE IF EXISTS tweet;

CREATE TABLE image (
       id INTEGER PRIMARY KEY,
       name VARCHAR(30),
       byte_count INTEGER,
       upload_datetime DATETIME
);

CREATE INDEX image_upload_datetime_idx ON image(upload_datetime);
CREATE INDEX image_name_idx ON image(name);

CREATE TABLE tweet (
       id INTEGER PRIMARY KEY,
       timestamp TIMESTAMP DEFAULT NULL,
       image_id INTEGER,
       tweet_id INTEGER DEFAULT NULL,
       tweeted INTEGER DEFAULT 0,
       FOREIGN KEY (image_id) REFERENCES image(id)
);

