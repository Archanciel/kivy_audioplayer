from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class AudioPlayPosButtonsGUI(BoxLayout):
	def setSoundFile(self, soundFilePathName):
		self.audioPlayPosButtons.initSoundFile(soundFilePathName)
		

class AudioPlayPosButtonsMainApp(App):
	def build(self):
		# IMPORTANT:
		# from audioplayposbuttons import AudioPlayPosButtons is not necessary
		# if #: import AudioPlayPosButtons audioplayposbuttons.AudioPlayPosButtons
		# is in audioplayposbuttons.kv file !
		Builder.load_file('audioplayposbuttons.kv')
		
		soundFilePathName = r"D:\Users\Jean-Pierre\Downloads\Audiobooks\mental_versus_conscience\#39 Comment équilibrer notre Mental et notre Conscience .mp3"
		audioGUI = AudioPlayPosButtonsGUI()
		audioGUI.setSoundFile(soundFilePathName)
		
		return audioGUI


if __name__ == '__main__':
	AudioPlayPosButtonsMainApp().run()
