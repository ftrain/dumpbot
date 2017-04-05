#!/bin/bash

# Make the DB
sqlite3 mlkshk.db < db.sql

# homebrew install find-utils
# Get all the images ./images and add them to SQLite
gfind ./images -type f -printf "INSERT INTO image ('name', 'byte_count', 'upload_datetime') VALUES ('%f',%s,'%TY-%Tm-%Td %TT');\n" | sqlite3 mlkshk.db

# Make the tweet table, which tracks the ids already tweeted so we can
# do threaded tweets and keep track of what has been posted.
sqlite3 mlkshk.db "INSERT INTO tweet (image_id) SELECT id FROM image ORDER BY upload_datetime ASC;"

