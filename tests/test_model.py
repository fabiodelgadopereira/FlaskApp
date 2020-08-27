import unittest
import sys
sys.path.append("..//cadastro//resources//")
from user import User

class TestSum(unittest.TestCase):

    def test_sum(self):
        c =   User(1, 'fabio', 'senha_teste')
        self.assertEqual(c.username, "fabio", "Deveria ser Fabio")

if __name__ == '__main__':
    unittest.main()

