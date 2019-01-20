import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('transfers.txt')
        self.assertEqual(g.get_vertex('719').adjacent_to, ['719', 'F09', 'G22'])
        self.assertEqual(g.get_vertex('235').adjacent_to, ['235', 'D24', 'R31'])

    def test_find_all_paths(self):
        g = Graph('transfers.txt')
        self.assertEqual(g.find_all_paths('639', 'Q01'), [['639', 'M20', 'Q01'], ['639', 'M20', 'R23', 'Q01'], \
                                                          ['639', 'Q01'], ['639', 'R23', 'M20', 'Q01'], ['639', 'R23', 'Q01']])



if __name__ == '__main__':
   unittest.main()
