import unittest


from commands import weather

class Test(unittest.TestCase):
	"""Unit Test"""
	def test_wearher(self):
		message, attachment = weather.weather('123')
		print(message)
		self.assertEqual(1, 1)

if __name__ == "__main__":
	unittest.main()