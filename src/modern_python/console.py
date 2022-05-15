import textwrap
import click
import requests

from . import __version__


@click.command()
@click.version_option(version=__version__)
@click.option('--lang',default='en',help="Language preference")
def main(lang):
    """The Moden Python project."""
    API_URL = f'https://{lang}.wikipedia.org/api/rest_v1/page/random/summary'
    try:
        with requests.get(API_URL) as response:
            response.raise_for_status()
            data = response.json()

        title = data["title"]
        extract = data["extract"]

        click.secho(title, fg="green")
        click.echo(textwrap.fill(extract))
    except requests.exceptions.HTTPError as error:
        print(error)
