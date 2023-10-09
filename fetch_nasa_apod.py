import requests
from environs import Env

from pathlib import Path

from download_image import download_image


def fetch_nasa_apod(token):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'start_date': '2023-09-01', 'api_key': token}
    response = requests.get(url, params=params)
    response.raise_for_status()
    apods = response.json()

    for apod_number, apod in enumerate(apods):
        download_image(apod['url'], f'images/nasa_apod{apod_number + 1}')


if __name__ == '__main__':
    Path('images').mkdir(exist_ok=True)
    env = Env()
    env.read_env()
    nasa_token = env.str('NASA_TOKEN')
    fetch_nasa_apod(nasa_token)
