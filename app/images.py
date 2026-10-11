from dotenv import load_dotenv
from imagekitio import ImageKit
import os

load_dotenv()

imageKit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY")
)