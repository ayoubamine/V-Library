# -*- coding: utf-8 -*-

class Alert():

	def __init__(self, parent):

		self.parent = parent

	def show(self, msg):
		'''
			Show alert message
		'''
		self.parent.msg.setText(msg)
		self.parent.alert__form.show()

	def hide(self):
		'''
			Hide alert message
		'''
		self.parent.alert__form.hide()
