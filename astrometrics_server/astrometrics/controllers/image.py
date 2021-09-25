import json

from flask import Blueprint

from services.image import fetch_nasa_image_of_the_day

API_PREFIX = '/api/v0'
image_bp = Blueprint('image_bp', __name__, url_prefix=API_PREFIX)


@image_bp.route('/apod')
def fetch_image_of_the_day():
    return fetch_nasa_image_of_the_day()
