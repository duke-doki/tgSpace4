from datetime import datetime

import requests

from environs import Env
from pathlib import Path

from download_image import download_image


def fetch_nasa_epic(token):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {'api_key': token}
    response = requests.get(url, params=params)
    response.raise_for_status()
    epics = response.json()

    for epic_number, epic in enumerate(epics):
        link = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png'
        date = datetime.fromisoformat(epic['date'])
        converted_date = date.strftime("%Y/%m/%d")
        image = epic['image']
        link = link.format(converted_date, image)
        download_image(link, f'images/epic{epic_number + 1}', params=params)


if __name__ == '__main__':
    Path('images').mkdir(exist_ok=True)
    env = Env()
    env.read_env()
    nasa_token = env.str('NASA_TOKEN')
    fetch_nasa_epic(nasa_token)
