import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph()
        self.assertEqual(g.get_vertex('J19N').adjacent_to, ['J20N', 'J17N', 'J16N'])
        self.assertEqual(g.get_vertex('706N').adjacent_to, ['707N', '705N'])

    def test_find_all_paths(self):
        g = Graph()
        self.assertEqual(g.find_all_paths('F01N', 'F03N'), [['F01N', 'F03N'], ['F01N', 'F02N', 'F03N']])





if __name__ == '__main__':
    unittest.main()
