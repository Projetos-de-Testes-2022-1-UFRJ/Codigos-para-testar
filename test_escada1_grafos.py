import unittest
from escada1 import escada

class TestEscada(unittest.TestCase):
  def test_CT1(self):
    result = escada(2, 2, [
                           [0, 1],
                           [0, 1]
    ])
    self.assertEqual(result, 'N')

  def test_CT2(self):
    result = escada(2, 4, [
                           [0, 0, 0,  1],
                           [0, 1, 0, 0]
    ])
    self.assertEqual(result, 'N')

  def test_CT3(self):
    result = escada(2, 2, [
                           [0, 0],
                           [0, 0]
    ])
    self.assertEqual(result, 'S')

  def test_CT4(self):
    result = escada(2, 3, [
                           [1, 1,  1],
                           [0, 0, 1]
    ])
    self.assertEqual(result, 'S')