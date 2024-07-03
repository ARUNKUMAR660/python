class Song:
    
    def __init__(self,name,artist,album,length):
        self.name=name
        self.artist=artist
        self.album=album
        self.length=length
        
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
        
    def get_artist(self):
        return self.artist
    def set_name(self,artist):
        self.artist=artist
        
    def get_album(self):
        return self.album
    def set_album(self,album):
        self.album=album
        
    def get_length(self):
        return self.length
    def set_length(self,length):
        self.length=length

class Playlist:
    def __init__(self,name):
        self.songs=[]  
        self.count=0
        self.name=name
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
    def add_song(self,mysong):
        if self.count<12:
            self.songs.append(mysong)
            self.count+=1
            print(f"songs {mysong.get_name()} add to my {self.name}")
        else:
            print("playlist is full cannot add songs")