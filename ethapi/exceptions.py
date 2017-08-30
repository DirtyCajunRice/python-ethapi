class UnimplementedException(Exception):
    """
    When running a method that hasn't been implemented upstream or downstream
    """
    def __str__(self):
        return "The requested operation is not implemented."
