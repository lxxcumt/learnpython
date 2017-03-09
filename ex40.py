class Song(object):
	
	def __init__(self, Songs, singer):
		self.Songs = Songs
		self.singer = singer
		
	def sing_me_a_song(self):
		for song in self.Songs:
			print song, singer
	
				
Songs = ["Shake It Off","Speak Now","Mine","innocent","You Belong With Me","Love story","back to december","our song"]
			
singer = "  --- Taylor Swift"
			
Taylor_song = Song()
						
Taylor_song.sing_me_a_song()

