from flask import current_app
from urllib.parse import urlparse


def format_nasa_api_url(api_url) -> str:
    """
    Format the give API URL by appending api_key (from config) as a query parameter.

    :param api_url: URL to format
    :return: Formatted URL
    """
    url_parts = urlparse(url=api_url)
    if not url_parts.query:
        api_url += f'?api_key={current_app.config["NASA_API_KEY"]}'
    else:
        api_url += f'&api_key={current_app.config["NASA_API_KEY"]}'

    return api_url
