import argparse
import os
import random
from time import sleep

import telegram
from environs import Env


def publish_directory_photos(directory, frequency, photo, chat_id):
    while True:
        images = os.listdir(directory)
        random.shuffle(images)
        if photo:
            with open(f'{directory}/{photo}', 'rb') as file:
                bot.send_document(chat_id=chat_id, document=file)
            sleep(frequency * 60 * 60)
            images.remove(photo)
        for image in images:
            with open(f'{directory}/{image}', 'rb') as file:
                bot.send_document(chat_id=chat_id, document=file)
            sleep(frequency * 60 * 60)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    tg_token = env.str('TG_TOKEN')
    bot = telegram.Bot(token=tg_token)

    parser = argparse.ArgumentParser(
        description='This program allows to start publishing '
                    'photos on telegram channel.')
    parser.add_argument('-p', '--photo',
                        help='enter the name of the first photo')
    parser.add_argument('-f', '--frequency',
                        help='type how often you want to publish in hours',
                        type=int, default=4)
    parser.add_argument('chat_id', help="enter your chat ID")
    args = parser.parse_args()

    publish_directory_photos('images', args.frequency, args.photo, args.chat_id)
