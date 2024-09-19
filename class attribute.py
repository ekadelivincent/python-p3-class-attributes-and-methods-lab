class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment song count
        Song.add_song_to_count()

        # Add to genres and artists
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

        # Update genre count and artist count
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Example Usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
wonderwall = Song("Wonderwall", "Oasis", "Rock")
single_ladies = Song("Single Ladies", "Beyonce", "Pop")
hotline_bling = Song("Hotline Bling", "Drake", "Rap")

# Check class attributes
print(Song.count)  # Outputs: 4
print(Song.artists)  # Outputs: ["Jay-Z", "Oasis", "Beyonce", "Drake"]
print(Song.genres)  # Outputs: ["Rap", "Rock", "Pop"]
print(Song.genre_count)  # Outputs: {"Rap": 2, "Rock": 1, "Pop": 1}
print(Song.artist_count)  # Outputs: {"Jay-Z": 1, "Oasis": 1, "Beyonce": 1, "Drake": 1} 