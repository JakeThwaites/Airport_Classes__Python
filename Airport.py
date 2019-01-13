from Flight import Flight

class Airport:
    def __init__(self, airport_code):
        self.code = airport_code
        self.hangar = []
        self.latest_flight_number = 0

    def create_flight(self, destination, required_passengers):
        self.latest_flight_number += 1
        newFlight = Flight(self.latest_flight_number, destination, required_passengers)
        self.hangar.append(newFlight)