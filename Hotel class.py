class Hotel:
    """Represents the hotel that manages rooms."""

    def __init__(self, name: str, location: str):
        self.__name = name  # Private attribute to store the hotel's name
        self.__location = location  # Private attribute to store the hotel's location
        self.__rooms = []  # Private list to store Room objects associated with the hotel

    def add_room(self, room):
        self.__rooms.append(room)  # Appends the given room to the list of rooms

    def remove_room(self, room):
        if room in self.__rooms:  # Checks if the room exists in the list before removing
            self.__rooms.remove(room)  # Removes the specified room from the list

    def get_available_rooms(self):
        return [room for room in self.__rooms if room.check_availability()]
        # Filters and returns rooms that have availability set to True

    def __str__(self):
        """Returns a string representation of the hotel, including its name, location, and number of rooms."""
        return f"Hotel: {self.__name}, Location: {self.__location}, Rooms: {len(self.__rooms)}"