#!/usr/bin/python3
"""Module 4-square: defines a square class with size, area, and printing.
"""


class Square:
    """Class that defines a square with size validation, area method,
    and a method to print the square.
    """

    def __init__(self, size=0):
        """Initialize the square with a private attribute size.

        Args:
            size (int): size of the square (default 0)
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.size = size  # use setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): new size of the square
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#' in stdout.
        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
