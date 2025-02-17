from PIL import Image
import requests
from io import BytesIO


def download_image(url):
  response = requests.get(url)
  response.raise_for_status()
  image = Image.open(BytesIO(response.content))
  return image