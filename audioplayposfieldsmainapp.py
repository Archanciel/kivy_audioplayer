from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class AudioPlayPosFieldsGUI(BoxLayout):
	def setSoundFile(self, soundFilePathName):
		self.audioPlayPosFields.initSoundFile(soundFilePathName)
		

class AudioPlayPosFieldsMainApp(App):
	def build(self):
		# IMPORTANT:
		# from audioplayposbuttons import AudioPlayPosFields is not necessary
		# if #: import AudioPlayPosFields audioplayposbuttons.AudioPlayPosFields
		# is in audioplayposbuttons.kv file !
		Builder.load_file('audioplayposfields.kv')
		Builder.load_file('audioplayposfieldsmain.kv')

		soundFilePathName = r"D:\Users\Jean-Pierre\Downloads\Audiobooks\mental_versus_conscience\#39 Comment équilibrer notre Mental et notre Conscience .mp3"
		audioGUI = AudioPlayPosFieldsGUI()
		audioGUI.setSoundFile(soundFilePathName)
		
		return audioGUI


if __name__ == '__main__':
	AudioPlayPosFieldsMainApp().run()
