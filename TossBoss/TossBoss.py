"""
Main implementation for the TossBoss results manager. Uses data stored in Athlete class to measure improvements and visualize data

Jack Hansen, Spring 2025

"""

import matplotlib.pyplot as plt
from Athlete import Athlete

def graph_throws(athlete, event):
    """
    Graphs throws for a specific athlete and event over time.

    Parameters:
        - athlete: An Athlete object.
        - event: The event to graph (e.g., 'hammer', 'shotput').
    """
    event_data = athlete.get_event_data(event)

    if not event_data:
        print(f"No data found for athlete {athlete.get_name()} in event {event}.")
        return

    # Extract and sort data by date
    dates, distances = zip(*sorted(event_data, key=lambda x: x[0]))

    # Plotting the data
    plt.figure(figsize=(10, 6))
    plt.plot(dates, distances, marker='o', label=f"{event} distances")
    plt.title(f"{athlete.get_name()}'s {event} Performance Over Time")
    plt.xlabel("Date")
    plt.ylabel("Distance (m)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Calculate and display average improvement
    avg_improvements = athlete.average_improvement()
    if event in avg_improvements:
        print(f"Average improvement for {event}: {avg_improvements[event]} meters")
    else:
        print(f"No average improvement data available for {event}.")

# Example usage
if __name__ == "__main__":
    athlete = Athlete("John Doe")
    athlete.read_from_csv("athlete_data.csv")
    graph_throws(athlete, "hammer")
