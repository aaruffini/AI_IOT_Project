from colorthief import ColorThief
import requests
from io import BytesIO

def colorExtract(url):
    try:
        print("Fetching album...")
        response = requests.get(url, timeout=1)
        response.raise_for_status()  # Ensure HTTP status is 200
        print("Image fetched successfully!")

        # Open the image
        album_thief = ColorThief(BytesIO(response.content))
        palette = album_thief.get_palette(color_count=3)
        print(palette)

    except Exception as e:
        print(f"Error: {e}")
        return []

