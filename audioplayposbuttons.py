from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock


class AudioPlayPosButtons(BoxLayout):
	def __init__(self, **kw):
		super().__init__(**kw)

		self.soundloaderSharedMp3Obj = None

		# WARNING: accessing MainWindow fields defined in kv file
		# in the __init__ ctor is no longer possible when using
		# ScreenManager. Here's the solution:
		# (https://stackoverflow.com/questions/26916262/why-cant-i-access-the-screen-ids)
		Clock.schedule_once(self._finish_init)

	def _finish_init(self, dt):
		"""
		Due to using WindowManager for managing multiple screens, the content
		of this method can no longer be located in the __init__ ctor method,
		but must be called by Clock.schedule_once() (located in the base
		class).

		:param dt:
		"""
#		self.soundloaderSharedMp3Obj = None
	
	def initSoundFile(self, soundFilePathName):
		if 'mp3' != soundFilePathName[-3:]:
			return
		
		self.sharedAudioFilePathNameInitValue = soundFilePathName
		self.soundloaderSharedMp3Obj = SoundLoader.load(soundFilePathName)
	
	def playSharedFile(self):
		"""
		Method called when pressing the share file Play button
		"""
		self.sharedFilePlayButton.disabled = True
		self.soundloaderSharedMp3Obj.play()
	
	def stopSharedFile(self):
		"""
		Method called when pressing the source file Stop button
		"""
		self.soundloaderSharedMp3Obj.stop()
		self.sharedFilePlayButton.disabled = False
	
	def backwardSharedFileTenSeconds(self):
		"""
		Method called when source file < button is pressed.
		"""
		currentPos = self.soundloaderSharedMp3Obj.get_pos()
		currentPos -= 10
		self.updateFileSoundPos(soundloaderMp3Obj=self.soundloaderSharedMp3Obj,
		                        newSoundPos=currentPos,
		                        soundFilePlayButton=self.sharedFilePlayButton)
	
	def backwardSharedFileThirtySeconds(self):
		"""
		Method called when source file << button is pressed.
		"""
		currentPos = self.soundloaderSharedMp3Obj.get_pos()
		currentPos -= 30
		self.updateFileSoundPos(soundloaderMp3Obj=self.soundloaderSharedMp3Obj,
		                        newSoundPos=currentPos,
		                        soundFilePlayButton=self.sharedFilePlayButton)
	
	def forwardSharedFileTenSeconds(self):
		"""
		Method called when source file > button is pressed.
		"""
		currentPos = self.soundloaderSharedMp3Obj.get_pos()
		currentPos += 10
		self.updateFileSoundPos(soundloaderMp3Obj=self.soundloaderSharedMp3Obj,
		                        newSoundPos=currentPos,
		                        soundFilePlayButton=self.sharedFilePlayButton)
	
	def forwardSharedFileThirtySeconds(self):
		"""
		Method called when source file >> button is pressed.
		"""
		currentPos = self.soundloaderSharedMp3Obj.get_pos()
		currentPos += 30
		self.updateFileSoundPos(soundloaderMp3Obj=self.soundloaderSharedMp3Obj,
		                        newSoundPos=currentPos,
		                        soundFilePlayButton=self.sharedFilePlayButton)
	
	def goToSharedFileStartPos(self):
		"""
		Method called when source file <| button is pressed.
		"""
		self.updateFileSoundPos(soundloaderMp3Obj=self.soundloaderSharedMp3Obj,
		                        newSoundPos=0,
		                        soundFilePlayButton=self.sharedFilePlayButton)
	
	def goToSharedFileEndPos(self):
		"""
		Method called when source file |> button is pressed.
		"""
		endPos = self.soundloaderSharedMp3Obj.length - 5
		self.updateFileSoundPos(soundloaderMp3Obj=self.soundloaderSharedMp3Obj,
		                        newSoundPos=endPos,
		                        soundFilePlayButton=self.sharedFilePlayButton)
	
	def updateFileSoundPos(self,
	                       soundloaderMp3Obj,
	                       newSoundPos,
	                       soundFilePlayButton):
		"""
		This method avoids duplicating several time the same code.

		:param soundloaderMp3Obj:
		:param newSoundPos:
		:param soundFilePlayButton:
		"""
		soundloaderMp3Obj.seek(newSoundPos)
		
		if soundloaderMp3Obj.status == 'stop':
			# here, the mp3 was played until its end
			soundloaderMp3Obj.play()
		
		soundFilePlayButton.disabled = True


if __name__ == '__main__':
	class AudioPlayPosButtonsMainApp(App):
		def build(self):
			Builder.load_file('audioplayposbuttons.kv')
			
			return AudioPlayPosButtons()
	
	
	AudioPlayPosButtonsMainApp().run()
