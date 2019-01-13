class Plane:
    def __init__(self, type, airline, max_passengers):
        self.type = type
        self.airline = airline
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def has_empty_seats(self):
        return len(self.passengers) < self.max_passengers