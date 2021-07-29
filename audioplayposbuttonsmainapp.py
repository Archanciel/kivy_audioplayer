from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class AudioPlayPosButtonsGUI(BoxLayout):
	pass

class AudioPlayPosButtonsMainApp(App):
	def build(self):
		# IMPORTANT:
		# from audioplayposbuttons import AudioPlayPosButtons is not necessary
		# if #: import AudioPlayPosButtons audioplayposbuttons.AudioPlayPosButtons
		# is in audioplayposbuttons.kv file !
		Builder.load_file('audioplayposbuttons.kv')

		return AudioPlayPosButtonsGUI()


if __name__ == '__main__':
	AudioPlayPosButtonsMainApp().run()
