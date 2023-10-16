import argparse
import os
import random
from time import sleep

import telegram
from environs import Env


def publish_all_photos(directory, frequency, chat_id):
    while True:
        images = os.listdir(directory)
        random.shuffle(images)

        for image in images:
            with open(f'{directory}/{image}', 'rb') as file:
                bot.send_document(chat_id=chat_id, document=file)
            sleep(frequency * 60 * 60)


def publish_one_photo(directory, photo, chat_id):
    with open(f'{directory}/{photo}', 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    tg_token = env.str('TG_TOKEN')
    bot = telegram.Bot(token=tg_token)

    parser = argparse.ArgumentParser(
        description='This program allows to start publishing '
                    'photos on telegram channel.')
    parser.add_argument('chat_id', help="enter your chat ID")
    parser.add_argument('-p', '--photo',
                        help='enter the name of the photo to publish',
                        type=str,
                        default=f'{random.choice(os.listdir("images"))}')
    parser.add_argument('-f', '--frequency',
                        help='type how often you want to publish in hours',
                        type=int, default=4)
    parser.add_argument('-a', '--all',
                        help='use if you want all images to be posted',
                        action='store_true')
    args = parser.parse_args()

    if args.all:
        publish_all_photos('images', args.frequency, args.chat_id)
    else:
        publish_one_photo('images', args.photo, args.chat_id)
