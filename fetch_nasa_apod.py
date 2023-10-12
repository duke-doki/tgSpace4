from pathlib import Path

import requests
from environs import Env

from download_image import download_image, fetch_file_extension


def fetch_nasa_apod(token, url):
    params = {'start_date': '2023-09-01', 'api_key': token}
    response = requests.get(url, params=params)
    response.raise_for_status()
    apods = response.json()

    for apod_number, apod in enumerate(apods, start=1):
        download_image(apod['url'], f'images/nasa_apod{apod_number}')


if __name__ == '__main__':
    url = 'https://api.nasa.gov/planetary/apod'
    Path('images').mkdir(exist_ok=True)
    env = Env()
    env.read_env()
    nasa_token = env.str('NASA_TOKEN')
    if fetch_file_extension(url):
        fetch_nasa_apod(nasa_token, url)
