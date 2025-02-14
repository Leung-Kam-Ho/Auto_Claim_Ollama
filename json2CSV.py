import json
import csv
from datetime import datetime
import os
import shutil

class JsonToCSVConverter:
    def __init__(self, json_file: str, csv_file: str, image_dir: str):
        self.json_file = json_file
        self.csv_file = csv_file
        self.image_dir = image_dir

    def convert(self):
        # Load JSON data
        with open(self.json_file, 'r') as f:
            data = [json.loads(line) for line in f]

        # Sort data by date_of_payment
        data.sort(key=lambda x: datetime.strptime(x['date_of_payment'], '%Y-%m-%d'))

        # Create a directory for copied images
        os.makedirs(self.image_dir, exist_ok=True)

        # Write to CSV
        with open(self.csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name_of_goods', 'currency', 'final_price', 'date_of_payment', 'image_path']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for index, item in enumerate(data, start=1):
                # Copy image to the new folder with a new name
                new_image_path = f'{self.image_dir}/item_{index}.png'
                shutil.copy(item['image_path'], new_image_path)
                item['image_path'] = new_image_path  # Update image path
                writer.writerow(item)


if __name__ == "__main__":
    json_file = 'auto_claim.json'
    csv_file = 'auto_claim.csv'
    image_dir = 'images'
    converter = JsonToCSVConverter(json_file, csv_file, image_dir)
    converter.convert()
