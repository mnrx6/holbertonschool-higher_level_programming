#!/usr/bin/python3
"""Module for writing and Reading file."""
import json


def serialize_and_save_to_file(data, filename):
    """Write and dump json file."""
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Read and load json file."""
    with open(filename, "r") as f:
        data = json.load(f)
        return data
