import unittest
from multiply.by_three import multiply_by_three

class TestMultiplyByThree(unittest.TestCase):

	def test_multiply_by_three(self):
		self.assertEqual(multiply_by_three(15), 9)

unittest.main()
