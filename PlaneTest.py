import unittest

from Passenger import Passenger
from Plane import Plane
from unittest import TestCase



class TestPlane(unittest.TestCase):
    def setUp(self):
        self.passenger = Passenger("Jake", 10)
        self.plane = Plane("Boeing 747", "Emirates", 2)

    def test_has_type(self):
        self.assertEqual("Boeing 747", self.plane.type)

    def test_has_airline(self):
        self.assertEqual("Emirates", self.plane.airline)

    def test_has_max_passengers(self):
        self.assertEqual(2, self.plane.max_passengers)

    def test_starts_with_no_passengers(self):
        self.assertEqual(0, len(self.plane.passengers))

    def test_can_add_passenger(self):
        self.assertEqual(0, len(self.plane.passengers))
        self.plane.add_passenger(self.passenger)
        self.assertEqual(1, len(self.plane.passengers))

if __name__ == '__main__':
    unittest.main()