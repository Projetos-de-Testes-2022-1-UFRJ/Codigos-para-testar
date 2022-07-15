import unittest
from baralho1 import baralho1

class TestBaralho(unittest.TestCase):

  def test_CT1(self):
    result = baralho1('10C10E01E01U01P')
    self.assertEqual(result, [12, 11, 12, 12])