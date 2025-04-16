from ollama_claim import ImageAnalyzer
from json2CSV import JsonToCSVConverter
from glob import glob
import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    image_paths = glob('item/*.jpeg') + glob('item/*.jpg') + glob('item/*.png') + glob('item/*.PNG')
    json_file = 'output/auto_claim.json'
    csv_file = 'output/auto_claim.csv'
    image_dir = 'output'
    logger.info(image_paths)
    # analyzer = ImageAnalyzer(image_paths)
    # analyzer.analyze_images(save_path=json_file)
    converter = JsonToCSVConverter(json_file, csv_file, image_dir)
    converter.convert()