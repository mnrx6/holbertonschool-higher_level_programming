#!/usr/bin/python3
"""Module for serializing custom objects."""

import pickle


class CustomObject:
    """Represent a custom object."""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initialize a custom object."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object information."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize object to a file."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize object from a file."""
        try:
            with open(filename, "rb") as f:
                data = pickle.load(f)
            return data
        except Exception:
            return None
