#!/usr/bin/python3

import unittest
import interest


class TestInterestCalculations(unittest.TestCase):

    def test_simple_interest(self):
        self.assertEqual(round(interest.interest('simple', 100, 0.10, 0), 5),
                         100)
        self.assertEqual(round(interest.interest('simple', 100, 0.10, 1), 5),
                         110)
        self.assertEqual(round(interest.interest('simple', 100, 0.10, 2), 5),
                         120)
        self.assertEqual(round(interest.interest('simple', 100, 0.10, 3), 5),
                         130)
        self.assertEqual(round(interest.interest('simple', 100, 0.10, 10), 5),
                         200)

    def test_compound_interest(self):
        self.assertEqual(round(interest.interest('compound', 100, 0.10, 0), 5),
                         100)
        self.assertEqual(round(interest.interest('compound', 100, 0.10, 1), 5),
                         110)
        self.assertEqual(round(interest.interest('compound', 100, 0.10, 2), 5),
                         121)
        self.assertEqual(round(interest.interest('compound', 100, 0.10, 3), 5),
                         133.1)
        self.assertEqual(round(interest.interest('compound', 100, 0.10, 10),
                               5), 259.37425)

if __name__ == '__main__':
    unittest.main()
