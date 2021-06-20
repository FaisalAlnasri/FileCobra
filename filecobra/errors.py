class DirectoryNotEmpty(Exception):
    """Exception raised when a user tries to delete a non-empty directory"""
    def __init__(self, message):
        self.message = message

if __name__ == "__main__":
    pass