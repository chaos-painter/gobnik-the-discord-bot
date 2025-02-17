import cv2
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data import *


def frameCapture(path):
  video = cv2.VideoCapture(path)
  count = 0
  success = True
  total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
  print(total_frames)
  while success:
    success, image = video.read()

    if not success or image is None:
      print(f"Could not read frame {count}")
      continue

    resized_image = cv2.resize(image, (51, 38), interpolation=cv2.INTER_AREA)
    
    output_path = os.path.join(DATA_PATH, f"frames", f"{count}.png")
    success_write = cv2.imwrite(output_path, resized_image)
    if not success_write:
      print(f"Failed to save frame {count}")
    count += 1


if __name__ == "__main__":
  frameCapture(f"{DATA_PATH}/bad_apple.mp4")
  print(f"{DATA_PATH}/bad_apple.mp4")

