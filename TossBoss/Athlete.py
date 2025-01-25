"""
Athlete class to manage and manipulate data for a variety of throwers, created for use in TossBoss

Jack Hansen, Spring 2025

"""

import csv

class Athlete:
    def __init__(self, name: str):
        """
        Initializes an Athlete object.

        Parameters:
            - name: The name of the athlete.
        """
        self._name = name
        self._event = ""
        self._data = []

    def add_throw(self, weight: float, throw: str, distance: float, date: str):
        """
        Adds a throw to the athlete's record.

        Parameters:
            - weight: The weight of the throw (in kg).
            - throw: The type of throw (e.g., 'hammer', 'shotput').
            - distance: The distance of the throw (in meters).
            - date: The date of the throw.
        """
        self._data.append({"weight": weight, "throw": throw, "distance": distance, "date": date})

    def set_event(self, new_event: str):
        """
        Sets or updates the athlete's event.

        Parameters:
            - new_event: The new event (e.g., 'hammer', 'shotput').
        """
        self._event = new_event

    def get_event_data(self, event: str):
        """
        Retrieves all throw data for a specific event.

        Parameters:
            - event: The event for which to retrieve data.

        Returns:
            - A list of dictionaries containing throw data for the event.
        """
        return [
            {"date": record["date"], "distance": record["distance"]}
            for record in self._data
            if record["throw"] == event
        ]

    def get_name(self):
        """
        Retrieves the athlete's name.

        Returns:
            - The name of the athlete.
        """
        return self._name

    def read_from_csv(self, csv_file: str):
        """
        Reads throw data from a CSV file and populates the athlete's records.

        Parameters:
            - csv_file: The path to the CSV file.
        """
        
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["name"] == self._name:
                    self.add_throw(
                        float(row["weight"]),
                        row["throw"],
                        float(row["distance"]),
                        row["date"]
                    )

    def average_improvement(self):
        """
        Calculates the average improvement for each event based on throw distances.

        Returns:
            - A dictionary mapping each event to its average improvement (in meters).
        """
        improvements = {}
        
        # Group throws by event
        throws_by_event = {}
        for record in self._data:
            event = record["throw"]
            if event not in throws_by_event:
                throws_by_event[event] = []
            throws_by_event[event].append(record["distance"])
        
        # Calculate average improvement for each event
        for event, distances in throws_by_event.items():
            if len(distances) > 1:
                improvements[event] = (max(distances) - min(distances)) / (len(distances) - 1)
        
        return improvements
