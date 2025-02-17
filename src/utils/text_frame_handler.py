import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data import *
from utils import *
from PIL import Image


def frames_to_text_frames():
  for image_path in sorted(IMAGE_FRAMES_PATH.glob("*.*")):
    with Image.open(image_path) as image:
      prepare_image(image, new_width=51, charset=ASCII_CHARS, path=f"{TEXT_FRAMES_PATH}/{image_path.stem}.txt")

import re
def load_text_frames():
  frames = []
  def extract_number(file_path):
    match = re.search(r'(\d+)', file_path.stem)
    return int(match.group(1)) if match else float('inf')
  
  for frame_path in sorted(TEXT_FRAMES_PATH.glob("*.txt"), key=extract_number):
    with open(frame_path, "r", encoding="utf-8") as file:
      frames.append(file.read())
  return frames


import time
import curses

def badapple(stdscr, frames):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(90)

    for frame in frames:
        stdscr.clear()
        stdscr.addstr(0, 0, frame)
        stdscr.refresh()
        time.sleep(0.033333333)

        if stdscr.getch() != -1:
            break

if __name__ == "__main__":
  # frames_to_text_frames()
  frames = load_text_frames()
  curses.wrapper(lambda stdscr: badapple(stdscr, frames))

