```
     █                       █               ▄
  ▄▄▄█  ▄   ▄  ▄▄▄▄▄  ▄▄▄▄   █▄▄▄    ▄▄▄   ▄▄█▄▄
 █▀ ▀█  █   █  █ █ █  █▀ ▀█  █▀ ▀█  █▀ ▀█    █
 █   █  █   █  █ █ █  █   █  █   █  █   █    █
 ▀█▄██  ▀▄▄▀█  █ █ █  ██▄█▀  ██▄█▀  ▀█▄█▀    ▀▄▄
                      █
```

This uploads a new image into a twitter thread whenever it runs.

1. The images are in `images/`

2. `./bootup.sh` makes the database and lists the images, and makes
the work table.

3. `tweetit.py` tweets an a new image whenever you run it.
   - You need python3
   - You need Twython installed (`pip install twython`).
   - You need an API key from Twitter and a token pair.

4. If you want to automate, you can set up a cronjob that runs
./tweetit.py every hour. When you set that up make sure you are
running it within the virtualenv context or whatever under which your
python is operating; i.e.

`cd dumpbot && source /Users/ford/envs/theenv/bin/activate && python tweetit.py`