import fullname
import unittest

class testCaseName(unittest.TestCase):
	def test_basic(self):
		self.assertEqual(fullname.name("Matthew","Hotchkiss"),"Matthew Hotchkiss")
		self.assertEqual(fullname.name("Harry","Potter"),"Harry Potter")
	def test_empty(self):
		self.assertEqual(fullname.name("",""), "")
		self.assertEqual(fullname.name("","Hotchkiss"),"Hotchkiss")
		self.assertEqual(fullname.name("Matthew",""),"Matthew")
	def test_inputs(self):
		self.assertEqual(fullname.name("AC","130"),"AC 130")
		self.assertEqual(fullname.name(AC,130),"AC 130")
		
		
