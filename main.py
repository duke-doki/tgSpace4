import os

import requests
from pathlib import Path
import pprint
from urllib.parse import urlsplit
from os.path import splitext
from environs import Env

env = Env()
env.read_env()

Path('images').mkdir(exist_ok=True)


# url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'


def download_image(url, directory):
    response = requests.get(url)
    response.raise_for_status()

    if fetch_file_extension(url):
        with open(f'{directory}{fetch_file_extension(url)}', 'wb') as image:
            image.write(response.content)


launch_id = '5eb87d47ffd86e000604b38a'
space_x_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'


def fetch_spacex_launch(url):
    response = requests.get(url)
    response.raise_for_status()
    images = response.json()['links']['flickr']['original']

    for image_number, image in enumerate(images):
        download_image(image, f'images/spacex{image_number + 1}')


def fetch_file_extension(url):
    parsed_link = urlsplit(url)
    root, extension = splitext(parsed_link.path)
    return extension


# fetch_file_extension('https://apod.nasa.gov/apod/image/2310/PlaneEclipse_Slifer_1756.jpg')

nasa_url = 'https://api.nasa.gov/planetary/apod'


def fetch_nasa_apod(url, token):
    params = {'start_date': '2023-09-01', 'api_key': token}
    response = requests.get(url, params=params)
    response.raise_for_status()
    apods = response.json()
    #pprint.pprint(apods, sort_dicts=False)

    for apod_number, apod in enumerate(apods):
        download_image(apod['url'], f'images/nasa_apod{apod_number + 1}')


fetch_spacex_launch(space_x_url)
nasa_token = env.str('NASA_TOKEN')
fetch_nasa_apod(nasa_url, nasa_token)
