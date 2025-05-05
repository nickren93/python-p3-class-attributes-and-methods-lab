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
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        for element in cls.genres:
            if element == genre:
                cls.add_to_genre_count(genre)
                return 
        cls.genres.append(genre)
        cls.genre_count.update({genre: 1})

    
    @classmethod
    def add_to_artists(cls, artist):
        for element in cls.artists:
            if element == artist:
                cls.add_to_artist_count(artist)
                return
        cls.artists.append(artist)
        cls.artist_count.update({artist: 1})

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] += 1

        
