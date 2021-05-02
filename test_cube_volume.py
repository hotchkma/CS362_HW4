import cube_volume 
import unittest
import math

class testCaseVolume(unittest.TestCase):
	def test_basics(self):
		self.assertEqual(cube_volume.volume(2),8)
		self.assertEqual(cube_volume.volume(1),1)
		self.assertEqual(cube_volume.volume(0),0)
	def test_nonbasics(self):
		self.assertEqual(cube_volume.volume(math.sqrt(2)),2*math.sqrt(2))
		self.assertEqual(cube_volume.volume(-3),-1)
	def test_inputs(self):
		self.assertEqual(cube_volume.volume('a'),-1)
		self.assertEqual(cube_volume.volume("5G"),-1)
		
		
