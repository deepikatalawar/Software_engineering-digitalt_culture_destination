import os
from pathlib import Path
import unittest

from cultural_destination import CulturalDestination

class TestCulturalDestination(unittest.TestCase):
    def test_workflow(self):
        # Define the path to the CSV file with the list of artists
        artists_csv_path = Path("artists.csv")

        # Define the path to the CSV file with the list of events
        events_csv_path = Path("events.csv")

        # Define the path to the output HTML file
        output_html_path = Path("cultural_destination_map.html")

        # Create a new CulturalDestination object
        cd = CulturalDestination()

        # Load the artists from the CSV file
        cd.load_artists_from_csv(artists_csv_path)

        # Load the events from the CSV file
        cd.load_events_from_csv(events_csv_path)

        # Generate the map and save it to an HTML file
        cd.generate_map(output_html_path)

        # Check that the HTML file was created
        self.assertTrue(output_html_path.is_file())

        # Open the HTML file in the default web browser
        os.startfile(output_html_path)

if __name__ == '__main__':
    unittest.main()
