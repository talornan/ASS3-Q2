import unittest

from main import weighted_round_robin


class TestWeightedRoundRobin(unittest.TestCase):

    def test_different_rights_different_items(self):
        rights = [1, 2, 4]
        valuations = [[11, 11, 22, 33, 44], [11, 22, 44, 55, 66], [11, 33, 22, 11, 66]]
        y = 0.5
        expected_out = [[3, 5, 66], [2, 4, 55], [3, 2, 33], [1, 3, 22], [3, 1, 11]]
        result = weighted_round_robin(rights, valuations, y)
        self.assertEqual(expected_out, result)

    def test_same_rights_different_items(self):
        valuations = [[1, 3, 1], [2, 40, 3], [1, 3, 2]]
        rights = [1, 2, 4]
        y = 0.5
        expected_out = [[3, 2, 3], [2, 3, 3], [3, 1, 1]]
        result = weighted_round_robin(rights, valuations, y)
        self.assertEqual(expected_out, result)

    def test_same_rights_same_items(self):
        valuations = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        y = 0.5
        rights = [1, 1, 1]
        expected_out = [[1, 1, 1], [2, 2, 1], [3, 3, 1]]
        result = weighted_round_robin(rights, valuations, y)
        self.assertEqual(expected_out, result)

    def test_different_rights_same_items(self):
        rights = [1, 2, 4]
        valuations = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        y = 0.5
        expected_out = [[3, 1, 1], [2, 2, 1], [3, 3, 1]]
        result = weighted_round_robin(rights, valuations, y)
        self.assertEqual(expected_out, result)

    def test_y_0(self):
        rights = [1, 2, 4]
        valuations = [[11, 11, 22, 33, 44], [11, 22, 44, 55, 66], [11, 33, 22, 11, 66]]
        y = 0
        expected_out = [[1, 5, 44], [2, 4, 55], [3, 2, 33], [3, 3, 22], [2, 1, 11]]
        result = weighted_round_robin(rights, valuations, y)
        self.assertEqual(expected_out, result)

    def test_y_1(self):
        rights = [1, 2, 4]
        valuations = [[11, 11, 22, 33, 44], [11, 22, 44, 55, 66], [11, 33, 22, 11, 66]]
        y = 1
        expected_out = [[3, 5, 66], [2, 4, 55], [3, 2, 33], [3, 3, 22], [1, 1, 11]]
        result = weighted_round_robin(rights, valuations, y)
        self.assertEqual(expected_out, result)


if __name__ == '__main__':
    unittest.main()
