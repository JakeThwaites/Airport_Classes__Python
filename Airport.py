from Flight import Flight

class Airport:
    def __init__(self, airport_code):
        self.code = airport_code
        self.hangar = []
        self.latest_flight_number = 0
        self.all_flights = []

    def create_flight(self, destination, required_passengers):
        self.latest_flight_number += 1
        newFlight = Flight(self.latest_flight_number, destination, required_passengers)
        self.all_flights.append(newFlight)

    def add_plane_to_flight(self, plane, flight):
        flight.add_plane(plane)

    def sell_ticket(self, passenger, flight):
        if flight.plane.has_empty_seats():
            flight.plane.add_passenger(passenger)
            passenger.buy_ticket()

