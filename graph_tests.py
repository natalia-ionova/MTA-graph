import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('transfers.txt')
        self.assertEqual(g.get_vertex('719').adjacent_to, ['719', 'F09', 'G22'])
        self.assertEqual(g.get_vertex('235').adjacent_to, ['235', 'D24', 'R31'])



if __name__ == '__main__':
   unittest.main()
