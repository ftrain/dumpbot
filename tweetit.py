import sqlite3
import dateutil.parser
from twython import Twython

# Put your stuff in here
APP_KEY = 'FILL_THIS_IN'
APP_SECRET = 'FILL_THIS_IN'
ACCESS_TOKEN = 'FILL_THIS_IN'
ACCESS_SECRET = 'FILL_THIS_IN'

# Put a tweet ID in here
# See https://twitter.com/ftrain/status/848534224600694784 for example
ORIGINAL_TWEET = 'THE_ID_OF_THE_TWEET_THAT_STARTS_THE_THREAD'
IMAGE_DIR = 'images/'
DB = 'mlkshk.db'


def dict_gen(curs):
    ''' From Python Essential Reference by David Beazley
    '''
    field_names = [d[0].lower() for d in curs.description]
    while True:
        rows = curs.fetchmany()
        if not rows:
            return
        for row in rows:
            yield dict(zip(field_names, row))


def __main__():
    # Log in to Twitter
    twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

    # Open up our DB
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    # Fetch the id of the last tweet posted, so that we can continue
    # the thread
    c.execute("""SELECT tweet_id
                 FROM tweet
                 WHERE tweet_id IS NOT NULL
                 ORDER BY timestamp
                 DESC LIMIT 1""")
    row = c.fetchone()

    last_tweet_id = ORIGINAL_TWEET
    if row is not None:
        last_tweet_id = row[0]

    dicts = dict_gen(c.execute("""
        SELECT image.name,
               image.upload_datetime,
               tweet.tweet_id,
               tweet.id
         FROM image
         LEFT OUTER JOIN tweet
           ON image.id = tweet.image_id
        WHERE tweet.tweeted = 0
        ORDER BY tweet.id ASC LIMIT 1"""))

    for d in dicts:
        date = dateutil.parser.parse(d['upload_datetime'])
        date_text = date.strftime('%A, %B %-d, %Y at %-I:%M %p')
        image = IMAGE_DIR + d['name']

        # If you want some text with each tweet this is a good place
        # to put it. I edited it out.
        tweet_text = """""".format(date_text)

        print("Posting image {}, with text '{}', in reply to {}"
              .format(image,
                      tweet_text,
                      last_tweet_id))

        image = open(image, 'rb')
        response = twitter.upload_media(media=image)
        updated = twitter.update_status(status=tweet_text,
                                        in_reply_to_status_id=last_tweet_id,
                                        media_ids=[response['media_id']])

        # get the twitter ID
        tweet_id = updated['id']

        # Update the table with the twitter ID
        c.execute("""
         UPDATE tweet
         SET tweet_id = :tweet_id,
             timestamp = CURRENT_TIMESTAMP,
             tweeted = 1
         WHERE id = :id""",
                  {'tweet_id': tweet_id, 'id': d['id']})
        # update the tweet
        conn.commit()

    c.close()

__main__()
