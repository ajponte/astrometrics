from astrometrics_server.astrometrics.util import format_nasa_api_url


def test_format_nasa_api_url():
    assert (format_nasa_api_url('https://api.nasa.gov/planetary/apod') ==
            'https://api.nasa.gov/planetary/apod?dodFNgy8MbtO3Hq1VDvFuGghfvwpOy99S4k6swkX')
    assert (format_nasa_api_url('https://api.nasa.gov/planetary/apod?foo=bar') ==
            'https://api.nasa.gov/planetary/apod?foo=bar&dodFNgy8MbtO3Hq1VDvFuGghfvwpOy99S4k6swkX')
