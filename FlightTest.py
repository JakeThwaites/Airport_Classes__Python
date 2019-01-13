import unittest

from Passenger import Passenger
from Plane import Plane
from Flight import Flight

class TestFlight(unittest.TestCase):

    def setUp(self):
        self.flight = Flight(1, "Glasgow", 3)
        self.plane = Plane("Boeing", "Emirates", 2)
        self.passenger = Passenger("Jake", 10)

    def test_has_flight_number(self):
        self.assertEqual(1, self.flight.flight_number)

    def test_has_destination(self):
        self.assertEqual("Glasgow", self.flight.destination)

    def test_has_required_passengers(self):
        self.assertEqual(3, self.flight.required_passengers)

    def test_can_add_plane(self):
        self.flight.add_plane(self.plane)
        self.assertEqual(self.plane, self.flight.plane)


if __name__ == '__main__':
    unittest.main()
