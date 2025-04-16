from pathlib import Path
from glob import glob
from ollama import chat
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ImageAnalyzer:
    def __init__(self, image_paths: list[str]):
        self.image_paths = image_paths
        self.json_data = {}
        self.failures = 0  # Initialize a counter for failures

    def analyze_images(self, save_path='auto_claim.json'):
        """Analyze images and save results to a JSON file."""
        # If folder of json file does not exist, create it
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        total_images = len(self.image_paths)
        for index, path in enumerate(self.image_paths):
            path = Path(path)
            # Verify the file exists
            if not path.exists():
                logger.error('Image not found at: %s', path)
                self.failures += 1  # Increment failure count
                continue  # Skip to the next image

            # Set up chat as usual
            response = chat(
                model="mistral-small3.1",
                format="json",  # Pass in the schema for the response
                messages=[
                    {
                        'role': 'user',
                        'content': """
                        Analyze this image and return a detailed JSON description
                        {
                            product : str # there is a lots of misleading information, please make sure the product name is correct, the name most likely is written near the product image and bold font
                            currency : str  # HKD, RMB, USD
                            actual_payment : float  # there is a lots of discount and shipping fee
                            date_of_payment : str  # yyyy-mm-dd
                        }
                        """,
                        'images': [path],
                    },
                ],
                options={'temperature': 0},  # Set temperature to 0 for more deterministic output
            )
            # Get only the content within {} and convert to json
            try:
                logger.info("Response: %s", response.message.content)
                self.json_data = json.loads(response.message.content)
                # Add the image path to the json data
                self.json_data['image_path'] = str(path)

                # Append the JSON data to a file
                with open(save_path, 'a') as f:
                    json.dump(self.json_data, f)
                    f.write('\n')

                # Show progress
                logger.info("Progress: %d/%d", index + 1, total_images)
            except Exception as e:
                logger.error(e)
                self.failures += 1  # Increment failure count

        # Log the total number of failures at the end
        logger.info("Total failures: %d", self.failures)


if __name__ == "__main__":
    image_paths = glob('item/*.jpeg') + glob('item/*.jpg') + glob('item/*.png')
    logger.info(image_paths)
    analyzer = ImageAnalyzer(image_paths)
    analyzer.analyze_images()
