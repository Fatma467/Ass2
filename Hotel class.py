# hotel.py
class Hotel:
    """Represents the hotel that manages rooms."""

    def __init__(self, name: str, location: str): #Initializes the hotel with a name, location, and an empty list of rooms.
        self.__name = name  # Private attribute to store the hotel's name
        self.__location = location  # Private attribute to store the hotel's location
        self.__rooms = []  # Private list to store Room objects associated with the hotel

    def add_room(self, room): #Adds a room to the hotel's list of rooms
        self.__rooms.append(room)  # Appends the given room to the list

    def get_available_rooms(self):#Returns a list of available rooms
        return [room for room in self.__rooms if room.check_availability()]
        # Filters and returns rooms that are available

    def __str__(self): #Returns a string representation of the hotel
        return f"Hotel: {self.__name}, Location: {self.__location}, Available Rooms: {len(self.get_available_rooms())}"

