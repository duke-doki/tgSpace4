from datetime import datetime
from pathlib import Path

import requests
from environs import Env

from download_image import download_image, fetch_file_extension


def fetch_nasa_epic(token, link):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {'api_key': token}
    response = requests.get(url, params=params)
    response.raise_for_status()
    epics = response.json()

    for epic_number, epic in enumerate(epics, start=1):
        date = datetime.fromisoformat(epic['date'])
        converted_date = date.strftime("%Y/%m/%d")
        image = epic['image']
        formated_link = link.format(converted_date, image)
        download_image(formated_link, f'images/epic{epic_number}', params=params)


if __name__ == '__main__':
    link = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png'
    Path('images').mkdir(exist_ok=True)
    env = Env()
    env.read_env()
    nasa_token = env.str('NASA_TOKEN')
    fetch_nasa_epic(nasa_token, link)
