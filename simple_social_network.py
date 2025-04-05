""" A simple social network for tracking connections between people"""

class Person:
    """ Represents a person in the social network
    
    Attributes:
        name (str): the person's name.
        connections (set of Person): other people in the social network who
            know this person.
    """
    def __init__(self, name):
        """Initialize a new Person object
        Args:
            name (str): name of the Person object
        """
        self.name = name
        self.connections = set()
