
import pylast
import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()
print("certfi where " + certifi.where())

# Specify the path to your certificate file
os.environ['SSL_CERT_FILE'] = '/path/to/ca-certificates.crt'


def login():
    try:
        # Read API credentials
        with open("API_KEYS") as f:
            API_KEY = f.readline().strip()
            API_SECRET = f.readline().strip()
            USERNAME = f.readline().strip()
            PASSHASH = pylast.md5(f.readline().strip())
            print(API_KEY)
            print(API_SECRET)
            print(USERNAME)
            print(PASSHASH)

        # Connect to Last.fm network
        network = pylast.LastFMNetwork(
            api_key=API_KEY,
            api_secret=API_SECRET,
            username=USERNAME,
            password_hash=PASSHASH
        )

        # Fetch top artists
    except FileNotFoundError:
        print("Error: 'API_KEYS' file not found. Please ensure it exists and contains valid credentials.")
    except pylast.NetworkError as e:
        print(f"NetworkError: {e}. Ensure your SSL certificates are correctly set up.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    try:
        user = network.get_user(USERNAME)
        now_playing = user.get_now_playing()
        if now_playing:
            print(f"Currently playing: {now_playing}")
            album = now_playing.get_album()
            if album:
                album_cover_url = album.get_cover_image()
                if album_cover_url:
                    print(f"Album Cover URL: {album_cover_url}")
                    return album_cover_url
                else:
                    print("No album cover available.")
            else:
                print("No album associated with the current track.")
        else:
            print("No track is currently playing.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Continuing")


if __name__ == "__main__":
    login()

