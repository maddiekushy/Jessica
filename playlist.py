
import csv


class Song:
    
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = int(duration)


class Playlist:
    
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_total_duration(self):
        total_seconds = 0

        for song in self.songs:
            total_seconds += song.duration

        minutes = total_seconds // 60
        seconds = total_seconds % 60

        print(f"{minutes:02d}:{seconds:02d}")

    def find_by_artist(self, artist_name):
        found = False

        for song in self.songs:
            if song.artist.lower() == artist_name.lower():
                print(song.title)
                found = True

        if not found:
            print(f"No songs found by {artist_name}.")

    def print_playlist(self):
        print(self.name.upper())

        for song in self.songs:
            print(f"{song.title} - {song.artist}")

    def load_songs(self, filename):
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                if not row or len(row) < 3:
                    continue

                # Skip the header row if present.
                if row[0].strip().lower() == "title":
                    continue

                title = row[0].strip()
                artist = row[1].strip()
                duration = int(row[2].strip())

                song = Song(title, artist, duration)
                self.add_song(song)
