import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials


if __name__ == "__main__":
    creds = open('client_credentials.txt', 'r')
    id, secret = creds.readlines()
    # extracting client id and secret for spotify api from text file in same dir

    client_credentials_manager = SpotifyClientCredentials(client_id=id,client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    # using spotipy for api requests

    track_list = open('tracks.txt', 'r').readlines()
    # reading list of track links from text file
    # for ease of use copy and paste tracks from a playlist

    for track_link in track_list:
        track_id = track_link.rstrip('\n').split('/')[4]
        # strip to obtain the id
        track = sp.track(track_id)
        album_cover_url = track['album']['images'][0]['url']
        # obtain album cover url from json received
        print(album_cover_url)
        # link to album cover image
        r = requests.get(album_cover_url, allow_redirects=True)
        open(album_cover_url.rsplit('/', 1)[1]+'.jpeg', 'wb').write(r.content)
        # saving to current directory
