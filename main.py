import argparse
import os
import random
from time import sleep

import telegram
from environs import Env


def publish_directory_photos(directory, frequency, photo):
    if not frequency:
        frequency = 4
    while True:
        images = os.listdir(directory)
        random.shuffle(images)
        if photo:
            bot.send_document(chat_id='@tgspace4',
                              document=open(f'{directory}/{photo}', 'rb'))
            sleep(frequency * 60 * 60)
            images.remove(photo)
        for image in images:
            bot.send_document(chat_id='@tgspace4',
                              document=open(f'{directory}/{image}', 'rb'))
            sleep(frequency * 60 * 60)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    tg_token = env.str('TG_TOKEN')
    bot = telegram.Bot(token=tg_token)

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--photo',
                        help='enter the name of the first photo')
    parser.add_argument('-f', '--frequency',
                        help='type how often you want to publish in hours',
                        type=int)
    args = parser.parse_args()

    publish_directory_photos('images', args.frequency, args.photo)
