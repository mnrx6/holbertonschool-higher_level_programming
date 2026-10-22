#!/usr/bin/python3
"""Fetch posts from an API and save them as CSV."""


import csv
import requests


def fetch_and_print_posts():
    """Fetch and print post titles."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts and save them to a CSV file."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()

        with open("posts.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()

            post_data = []

            for post in posts:
                data_to_add = {
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                }
                post_data.append(data_to_add)

            writer.writerows(post_data)
