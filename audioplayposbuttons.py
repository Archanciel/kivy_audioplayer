from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class AudioPlayPosButtons(BoxLayout):
	pass

if __name__ == '__main__':
	class AudioPlayPosButtonsMainApp(App):
		def build(self):
			Builder.load_file('audioplayposbuttons.kv')
			
			return AudioPlayPosButtons()
	
	
	AudioPlayPosButtonsMainApp().run()
