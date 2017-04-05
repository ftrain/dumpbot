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

2. You need the GNU find. If you're on a Mac, do `homebrew install findutils`;
this now runs as gfind.

3. `./bootup.sh` makes the database and lists the images, and makes
the work table. It does this by piping SQL directly into SQLite3.

4. `tweetit.py` tweets an a new image whenever you run it.
   - You need python3
   - You need Twython installed (`pip install twython`).
   - You need an API key from Twitter and a token pair.

5. If you want to automate, you can set up a cronjob that runs
`./tweetit.py` every hour.

6. When you set that up make sure you are running the cronjob within
the virtualenv context or whatever under which your python is
operating; i.e. `cd dumpbot && source /Users/ford/envs/theenv/bin/activate && python tweetit.py` this note
is just here to save you time, because I know you hardly ever set
up cronjobs and it's always hard to get the environment correct.

