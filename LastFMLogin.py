
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
        top_artists = network.get_top_artists(limit=5)  # Example: Fetch top 5 artists
        print("Top Artists:")
        for artist in top_artists:
            print(f"{artist.item.name} - {artist.weight} plays")

    except FileNotFoundError:
        print("Error: 'API_KEYS' file not found. Please ensure it exists and contains valid credentials.")
    except pylast.NetworkError as e:
        print(f"NetworkError: {e}. Ensure your SSL certificates are correctly set up.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    login()

