import requests

from urllib.parse import urlsplit
from os.path import splitext


def download_image(url, directory, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()

    if fetch_file_extension(url):
        with open(f'{directory}{fetch_file_extension(url)}', 'wb') as image:
            image.write(response.content)


def fetch_file_extension(url):
    parsed_link = urlsplit(url)
    root, extension = splitext(parsed_link.path)
    return extension
