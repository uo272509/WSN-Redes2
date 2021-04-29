class NonExistentDatabase(Exception):
    """
    Exception raised when the database file does not exist

    Attributes:
        name -- name of the database
    """
    def __init__(self, name):
        self.name = name
        super().__init__("The file \"" + name + "\" does not exist")
