from Passenger import Passenger
from Plane import Plane
from Flight import Flight

passenger = Passenger("Jake", 10)
plane = Plane("Boeing", "Emirates", 3)
flight = Flight(1, "Glasgow", 3)


flight.add_plane(plane)

test = flight.plane

print(test)