#!/usr/bin/python3
"""Generate personalized invitations from a template."""


def generate_invitations(template, attendees):
    """Generate invitation files for attendees."""

    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not all(isinstance(person, dict) for person in attendees):
        print("Error: All attendees must be dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, person in enumerate(attendees, start=1):
        invitation = template

        for key in ("name", "event_title", "event_date", "event_location"):
            value = person.get(key)

            if value is None or value == "":
                value = "N/A"

            invitation = invitation.replace(
                "{" + key + "}", str(value)
            )

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(invitation)
        except OSError as error:
            print(f"Error writing {filename}: {error}")
