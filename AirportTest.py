import unittest
from Plane import Plane
from Flight import Flight
from Passenger import Passenger
from Airport import Airport

class TestAirport(unittest.TestCase):
    def setUp(self):
        self.plane1 = Plane("Boeing", "Emirates", 2)
        self.passenger1 = Passenger("Jake", 10)
        self.airport = Airport("EDU")

    def test_has_code(self):
        self.assertEqual("EDU", self.airport.code)

    def test_starts_with_empty_hangar(self):
        self.assertEqual(0, len(self.airport.hangar))

    def test_can_create_flight(self):
        self.assertEqual(0,len(self.airport.all_flights))
        self.airport.create_flight("Glasgow,", 3)
        self.assertEqual(1, len(self.airport.all_flights))

    def test_latest_flight_number_auto_updates(self):
        self.assertEqual(0, self.airport.latest_flight_number)
        self.airport.create_flight("Glasgow", 3)
        self.assertEqual(1, self.airport.latest_flight_number)

    def test_can_add_plane_to_flight(self):
        self.airport.create_flight("Glasgow", 3)
        flight = self.airport.all_flights[0]
        self.airport.add_plane_to_flight(self.plane1, flight)
        self.assertEqual(self.plane1, flight.plane)

    def test_can_sell_ticket_for_flight(self):
        self.airport.create_flight("Glasgow", 3)
        flight = self.airport.all_flights[0]
        self.airport.add_plane_to_flight(self.plane1, flight)
        self.assertEqual( 0, len(flight.plane.passengers) )
        self.airport.sell_ticket(self.passenger1, flight)
        self.assertEqual( 1, len(flight.plane.passengers) )

if __name__ == '__main__':
     unittest.main()
