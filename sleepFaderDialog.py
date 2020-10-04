#coding:utf-8

from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QStyle
from PySide2.QtGui import QIcon
from PySide2.phonon import Phonon

class SleepFaderDialogInstance(QWidget):

	def __init__(self):

		super(SleepFaderDialogInstance, self).__init__()

		self.setGeometry(600, 400, 200, 200)
		self.setWindowTitle("Sleep Fader")

		self._initUI()


	def _initUI(self):

		layout = QHBoxLayout(self)
		self.playButton = QPushButton(self)
		self.playButton.setGeometry(100, 50, 30, 30)
		self.playButton.setIcon( self.style().standardIcon(QStyle.SP_MediaPlay) )
		self.playButton.clicked.connect(self.playMedia)
		layout.addWidget(self.playButton)


	def _initMedia(self):
		"""
		"""
		self.media =MediaObject(self)
		self.media.setCurrentSource(MediaSource("/audio/trap.wav"))
		audio =AudioOutput(MusicCategory, self)
		path =createPath(media, audio)

	def playMedia(self):
		self.media.play()