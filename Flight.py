class Flight:
   def __init__(self, flight_number, destination, required_passengers):
    self.flight_number = flight_number
    self.destination = destination
    self.required_passengers = required_passengers
    self.plane = None

   def change_flight_number(self, number):
      self.flight_number = number

   def add_plane(self, plane):
      self.plane = plane




