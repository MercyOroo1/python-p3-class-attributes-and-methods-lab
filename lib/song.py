class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__ (self,name,artist,genre):
        self.name = name 
        self.artist = artist
        self.genre = genre
        self.add_to_count()
        self.add_to_genre(self.genre)
        self.add_to_artists(self.artist)
        self.add_to_genre_count(self.genre)
        self.add_to_artist_count(self.artist)

    @classmethod
    def add_to_count(cls):
        Song.count += 1
    
    @classmethod
    def add_to_genre(cls,genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        else:
            print ("Genre already exists")
    
    @classmethod
    def add_to_artists(cls,artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        else:
            print ("Artist already exists")
    
    @classmethod
    def add_to_genre_count (cls,genre):
        if genre in cls.genre_count:
           cls.genre_count[genre] += 1
        else:
           cls.genre_count[genre] = 1
    
    @classmethod 
    def add_to_artist_count (cls,artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] +=1
        else:
            cls.artist_count[artist] = 1
           

