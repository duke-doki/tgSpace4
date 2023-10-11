import telegram
from environs import Env
import random
import os
from time import sleep
import argparse


def publish_directory_photos(directory, frequency):
    if not frequency:
        frequency = 4
    while True:
        images = os.listdir(directory)
        for image in images:
            bot.send_document(chat_id='@tgspace4',
                              document=open(f'{directory}/{image}', 'rb'))
            sleep(frequency * 60 * 60)
        random.shuffle(images)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    tg_token = env.str('TG_TOKEN')
    bot = telegram.Bot(token=tg_token)

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--frequency',
                        help='type how often you want to publish in hours',
                        type=int)
    args = parser.parse_args()

    publish_directory_photos('images', args.frequency)
