# Space Telegram

This program allows user to download images of space by SpaceX an NASA and publish them in
telegram channel via chatbot.

To download images from SpaceX launch use `fetch_spacex_launch`:
```
python fetch_spacex_launch.py {id of launch}
```
To download images from NASA use:
```
python fetch_nasa_{epic/apod}.py
```
For publishing images in telegram channel, please, read the description
using the following command:
```
python tgbot_publisher.py -h
```

### How to install

To download images from NASA you may need a token which can be accessed [here](https://api.nasa.gov/). You also
need to create a chatbot to get its token with [BotFather](https://telegram.me/BotFather). The tokens must be stored in `.env`
file which will look like this:
```
NASA_TOKEN={your token}
TG_TOKEN={your token}
```
You also need to create a telegram channel for its chat ID which will look like:
```
@{your chat id}
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).