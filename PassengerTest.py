import unittest

from Passenger import Passenger
from unittest import TestCase


class TestPassenger(unittest.TestCase):
    def setUp(self):
        self.passenger = Passenger("Jake")

    def test_has_name(self):
        self.assertEqual("Jake", self.passenger.name)


if __name__ == '__main__':
    unittest.main()
