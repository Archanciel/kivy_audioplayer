from kivy.uix.boxlayout import BoxLayout

from audioplayposbuttons import AudioPlayPosButtons


class AudioPlayPosFields(BoxLayout):
	def __init__(self, **kw):
		super().__init__(**kw)
		
	def initSoundFile(self, soundFilePathName):
		self.audioPlayPosButtons.initSoundFile(soundFilePathName)