from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class AudioPlayPosButtonsGUI(BoxLayout):
	pass

class AudioPlayPosButtonsMainApp(App):
	def build(self):
		from audioplayposbuttons import AudioPlayPosButtons
		Builder.load_file('audioplayposbuttons.kv')

		#Builder.load_file('audioplayposbuttonsmain.kv')

		return AudioPlayPosButtonsGUI()


if __name__ == '__main__':
	AudioPlayPosButtonsMainApp().run()
