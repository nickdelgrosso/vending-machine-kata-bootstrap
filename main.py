import pytest

class VendingMachineTestCase(unittest.TestCase):
  # Any function inside this class whose name 
  # starts with 'test...' is a test
  def test_the_answer(self):
    self.assertEqual(42, "fixme")

if __name__ == '__main__':
  unittest.main()
