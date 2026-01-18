#!/usr/bin/python3
"""Module 2-square: defines a square class with area calculation"""


class Square:
    """Class that defines a square by its size and can compute area"""

    def __init__(self, size=0):
        """Initialize the square with a private attribute size

        Args:
            size (int): size of the square (default 0)
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Compute and return the area of the square"""
        return self.__size ** 2
