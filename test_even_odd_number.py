class EvenOddNumber(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(even_odd_number(6))

    def test_odd_number(self):
        self.assertFalse(even_odd_number(3))