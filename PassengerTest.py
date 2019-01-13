import unittest

from Passenger import Passenger
from unittest import TestCase


class TestPassenger(unittest.TestCase):
    def setUp(self):
        self.passenger = Passenger("Jake", 10)

    def test_has_name(self):
        self.assertEqual("Jake", self.passenger.name)

    def test_has_money(self):
        self.assertEqual(10, self.passenger.money)

if __name__ == '__main__':
    unittest.main()
