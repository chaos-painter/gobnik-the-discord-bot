import PIL.Image
from data import *


ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", " "]


ASCII_CHARS_BLOCK = ["█", "▓", "▒", "░", " "]

ASCII_CHARS_BLOCK = ["⬛", "⚫", "🖤", "🔳", "🤍", "⚪", "⬜"]





def resize_image(image, new_width=100):
  width, height = image.size
  ratio = height / width
  new_height = int(new_width * ratio)
  resized_image = image.resize((new_width, new_height))
  return resized_image


def grayify(image):
  grayscale_image = image.convert("L")
  return grayscale_image


def pixels_to_ascii(image, charset=ASCII_CHARS):
  pixels = image.getdata()
  characters = "".join([charset[int(pixel / 255 * (len(charset) - 1))] for pixel in pixels])
  return characters


def process_image(image, new_width=100, charset=ASCII_CHARS):
  image = resize_image(image, new_width)
  image = grayify(image)
  return pixels_to_ascii(image, charset)


def format_ascii_image(characters, new_width=100):
  pixel_count = len(characters)
  ascii_image = "\n".join(characters[i:i+new_width] for i in range(0, pixel_count, new_width))
  return ascii_image


def prepare_image(image, new_width=100, charset=ASCII_CHARS, path=f"{DATA_PATH}/ascii_image.txt"):
  ascii_image = process_image(image, new_width, charset)
  ascii_image = format_ascii_image(ascii_image, new_width)
  with open(path, "w", encoding="utf-8") as file:
    file.write(ascii_image)



# from image_load import *
# if __name__ == "__main__":
  # image = download_image("https://i.ytimg.com/vi/ThHvx5a9IYA/maxresdefault.jpg")
  # ascii_image = format_ascii_image(process_image(image), 100)
  # print(ascii_image)
  # print(len(ascii_image))

  

