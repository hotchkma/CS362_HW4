import list_avg 
import unittest
import math

class testCaseAvg(unittest.TestCase):
	def test_filled(self):
		self.assertEqual(list_avg.avg([4,4,4,4,4]),4)
		self.assertEqual(list_avg.avg([1,2,3,4,5]),3)
		self.assertEqual(list_avg.avg([1,1,1,1,2]),1.2)
		self.assertEqual(list_avg.avg([1.1,1.2,1.4]),3.7/3.0)
	def test_empty(self):
		self.assertEqual(list_avg.avg([]),0)	
	def test_notnumbers(self):
		self.assertEqual(list_avg.avg(['a','b','c','d','e']),0)
		
		
