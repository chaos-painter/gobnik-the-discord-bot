from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent


DATA_PATH = BASE_DIR / "data"

IMAGE_FRAMES_PATH = DATA_PATH / "frames"

TEXT_FRAMES_PATH = DATA_PATH / "text_frames"
