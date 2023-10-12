import requests

import argparse
from pathlib import Path

from download_image import download_image


def fetch_spacex_launch(url):
    response = requests.get(url)
    response.raise_for_status()
    images = response.json()['links']['flickr']['original']

    for image_number, image in enumerate(images, start=1):
        download_image(image, f'images/spacex{image_number}')


if __name__ == '__main__':
    Path('images').mkdir(exist_ok=True)
    parser = argparse.ArgumentParser(
        description='This program allows to fetch images of SpaceX launch.')
    parser.add_argument('--id', help='Enter an id of the launch')
    args = parser.parse_args()
    if args.id:
        launch_id = args.id
    else:
        launch_id = '5eb87d47ffd86e000604b38a'

    space_x_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    fetch_spacex_launch(space_x_url)
