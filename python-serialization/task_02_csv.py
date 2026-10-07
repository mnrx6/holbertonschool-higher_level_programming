#!/usr/bin/python3
"""Convert CSV data to JSON."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV data to JSON."""
    try:
        with open(csv_filename, "r") as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open("data.json", "w") as f:
            json.dump(data, f)

        return True
    except Exception:
        return False
