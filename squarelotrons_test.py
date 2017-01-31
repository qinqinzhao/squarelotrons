import unittest
from squarelotrons import*

class squarelotrons(unittest.TestCase):

    def test_make_squarelotron(self):
        list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,\
                           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\
                           21, 22, 23, 24, 25]
        self.assertEqual(make_squarelotron(list_of_numbers),
                         [[1, 2, 3, 4, 5],
                          [6, 7, 8, 9, 10],
                          [11, 12, 13, 14, 15],
                          [16, 17, 18, 19, 20],
                          [21, 22, 23, 24, 25]])

    def test_make_list(self):
        squarelotron = [[1, 2, 3, 4, 5],
                        [6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15],
                        [16, 17, 18, 19, 20],
                        [21, 22, 23, 24, 25]]
        self.assertEqual(make_list(squarelotron),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,\
                          11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\
                          21, 22, 23, 24, 25])

    def test_upside_down_flip(self):
        squarelotron = [[1, 2, 3, 4, 5],
                        [6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15],
                        [16, 17, 18, 19, 20],
                        [21, 22, 23, 24, 25]]
        self.assertEqual(upside_down_flip(squarelotron, 'outer'),
                         [[21, 22, 23, 24, 25],
                          [16, 7, 8, 9, 20],
                          [11, 12, 13, 14, 15],
                          [6, 17, 18, 19, 10],
                          [1, 2, 3, 4, 5]])
        squarelotron = [[1, 2, 3, 4, 5],
                        [6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15],
                        [16, 17, 18, 19, 20],
                        [21, 22, 23, 24, 25]]
        self.assertEqual(upside_down_flip(squarelotron, 'inner'),
                         [[1, 2, 3, 4, 5],
                          [6, 17, 18, 19, 10],
                          [11, 12, 13, 14, 15],
                          [16, 7, 8, 9, 20],
                          [21, 22, 23, 24, 25]])

    def test_left_right_flip(self):
        squarelotron = [[1, 2, 3, 4, 5],
                        [6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15],
                        [16, 17, 18, 19, 20],
                        [21, 22, 23, 24, 25]]
        self.assertEqual(left_right_flip(squarelotron, 'outer'),
                         [[5, 4, 3, 2, 1],
                          [10, 7, 8, 9, 6],
                          [15, 12, 13, 14, 11],
                          [20, 17, 18, 19, 16],
                          [25, 24, 23, 22, 21]])
        squarelotron = [[1, 2, 3, 4, 5],
                        [6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15],
                        [16, 17, 18, 19, 20],
                        [21, 22, 23, 24, 25]]
        self.assertEqual(left_right_flip(squarelotron, 'inner'),
                         [[1, 2, 3, 4, 5],
                          [6, 9, 8, 7, 10],
                          [11, 14, 13, 12, 15],
                          [16, 19, 18, 17, 20],
                          [21, 22, 23, 24, 25]])

    def test_main_diagonal_flip(self):
        squarelotron = [[1, 2, 3, 4, 5],
                        [6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15],
                        [16, 17, 18, 19, 20],
                        [21, 22, 23, 24, 25]]
        self.assertEqual(main_diagonal_flip(squarelotron, 'outer'),
                         [[1, 6, 11, 16, 21],
                          [2, 7, 8, 9, 22],
                          [3, 12, 13, 14, 23],
                          [4, 17, 18, 19, 24],
                          [5, 10, 15, 20, 25]])
        squarelotron = [[1, 2, 3, 4, 5],
                        [6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15],
                        [16, 17, 18, 19, 20],
                        [21, 22, 23, 24, 25]]
        self.assertEqual(main_diagonal_flip(squarelotron, 'inner'),
                         [[1, 2, 3, 4, 5],
                          [6, 7, 12, 17, 10],
                          [11, 8, 13, 18, 15],
                          [16, 9, 14, 19, 20],
                          [21, 22, 23, 24, 25]])

    def test_inverse_diagonal_flip(self):
        squarelotron = [[1, 2, 3, 4, 5],
                        [6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15],
                        [16, 17, 18, 19, 20],
                        [21, 22, 23, 24, 25]]
        self.assertEqual(inverse_diagonal_flip(squarelotron, 'outer'),
                         [[25, 20, 15, 10, 5],
                          [24, 7, 8, 9, 4],
                          [23, 12, 13, 14, 3],
                          [22, 17, 18, 19, 2],
                          [21, 16, 11, 6, 1]])
        squarelotron = [[1, 2, 3, 4, 5],
                        [6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15],
                        [16, 17, 18, 19, 20],
                        [21, 22, 23, 24, 25]]
        self.assertEqual(inverse_diagonal_flip(squarelotron, 'inner'),
                         [[1, 2, 3, 4, 5],
                          [6, 19, 14, 9, 10],
                          [11, 18, 13, 8, 15],
                          [16, 17, 12, 7, 20],
                          [21, 22, 23, 24, 25]])

unittest.main()
