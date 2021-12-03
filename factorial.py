# this is only a testing file for using Github
import unittest

def factorial(n):
	""" return n! using a recursive solution"""
	if n==1:
		return 1
	else:
		return n*factorial(n-1)

class FactorialTest(unittest,TestCase):
	def test_factorial(self):
		self.assertEqual(factorial(1),1)
		self.assertEqual(factorial(2),2)
		
if __name__ == "__main__":
	unittest.main(exit=False)
