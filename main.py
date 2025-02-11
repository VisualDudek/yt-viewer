import atexit
import yaml
import logging
import logging.config
import sys
import os
import data_model

from dotenv import load_dotenv
from googleapiclient.discovery import build
from pydantic import ValidationError


# Load the logger config file
with open('logging_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

# Configure the logging module with the config file
logging.config.dictConfig(config)

# Get a logger object
logger = logging.getLogger(__name__)

# For the following part of code check readme multi-threaded/process part 
# Start the queue listener if Pyhon 3.12 or later
if sys.version_info >= (3, 12):
    queue_handler = logging.getHandlerByName('queue_handler')
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)
else:
    logger.warning('.getHandlerByName is not available in this version of Python')


def main():
    # Get API key from .env file
    logger.info('Getting API key from .env file')
    load_dotenv()
    API_KEY_YT = os.getenv('API_KEY_YT')

    # Build the youtube object
    youtube = build('youtube', 'v3', developerKey=API_KEY_YT)

    # --- TESTING THE YOUTUBE API ---

    # WARNING: There is a dfferece between channel_id and playlist_id !!! first two letters are different
    channel_id = 'UCaiL2GDNpLYH6Wokkk1VNcg'
    playlist_id = 'UUaiL2GDNpLYH6Wokkk1VNcg'

    # Create a request object to retrieve playlist items
    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=5
    )

    response = request.execute()
    res = response['items'][0]

    try:
        playlist_item = data_model.PlaylistItem(**res)
        playlist_response = data_model.PlaylistItemListResponse(**response)
    except ValidationError as e:
        print(e)

    pretty_json = playlist_item.model_dump_json(indent=2)

    print(pretty_json)
    logger.debug(playlist_item.snippet.title, extra={'snippet': playlist_item.snippet})

    pass


if __name__ == '__main__':
    main()