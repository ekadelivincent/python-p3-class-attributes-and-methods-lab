class Song:
   
    count = 0
    genre_count = {}  
    artist_count = {}  

  
    genres = genre_count
    artists = artist_count

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()  
        self.add_genre_count(self.genre)  
        self.add_to_artist_count(self.artist)  

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment 

    @classmethod
    def add_genre_count(cls, genre):
       
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



song1 = Song("Song A", "Hall and Oates", "Rap")
song2 = Song("Song B", "Beyonce", "Pop")
song3 = Song("Song D", "Jay Z", "Rock")


print("Genre Count:", Song.genres)  
print("Artist Count:", Song.artists)  
print("Total Songs:", Song.count)  