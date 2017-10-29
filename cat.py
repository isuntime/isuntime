import pygame
class cat:
	def __init__(self):
		pygame.mixer.init()
		track=pygame.mixer.music.load("a.wav")
		
	def run(self,htime,stimes):
		if htime in [1,29,59] and stimes in [1,29,59]:
			pygame.mixer.music.play()
		else:
			pass
if(__name__=='__main__'):
	pass

