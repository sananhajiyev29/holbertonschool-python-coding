#!/usr/bin/python3
"""Module 0-square: defines a square class with private size attribute"""


class Square:
    """Class that defines a square by its size"""

    def __init__(self, size):
        """Initialize the square with a private attribute size"""
        self.__size = size
