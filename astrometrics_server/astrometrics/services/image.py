import requests

from flask import current_app

from error import AstrometricsError
from util import format_nasa_api_url


def fetch_nasa_image_of_the_day() -> dict:
    """
    Makes an external call to api.nasa.gov to fetch the image of the day.

    :return: Image of the day.
    """
    try:
        res = requests.get(url=format_nasa_api_url(current_app.config['NASA_APOD_API']))
        return res.json()
    except Exception as e:
        raise AstrometricsError(f"Unknown error fetching APOD API: {e}")
