import unittest
from baralho1 import baralho1

class TestBaralho(unittest.TestCase):
  def test_CT1(self):
    result = baralho1('01C')
    self.assertEqual(result, [12, 13, 13, 13])
  
  def test_CT2(self):
    result = baralho1('01C02C03C04C05C06C07C08C09C10C11C12C13C01E02E03E04E05E06E07E08E09E10E11E12E13E01U02U03U04U05U06U07U08U09U10U11U12U13U01P02P03P04P05P06P07P08P09P10P11P12P13P')
    self.assertEqual(result, [0, 0, 0, 0])

  def test_CT3(self):
    result = baralho1('01C01C02E02E03U03U04P04P')
    self.assertEqual(result, ['erro', 'erro', 'erro', 'erro'])


    