from __future__ import print_function

import unittest
from collections import Counter

from weighted_choice import weighted_choice


class TestWeightedChoice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seq = ['a', 'b', 'c', 'd']
        cls.weights = [0.5, 0.2, 0.1, 0.1]
        cls.iterations = 1000

    def test_probabilities(self):
        counter = Counter(weighted_choice(self.seq, self.weights)
                          for _ in range(self.iterations))
        print(counter)

if __name__ == '__main__':
    unittest.main()
