# Image Analysis and CSV Conversion

## Overview
This project analyzes images and converts the results into a CSV format. It utilizes the `ImageAnalyzer` class to process images and the `JsonToCSVConverter` class to convert the JSON output into a CSV file.

## Requirements
You can install the required libraries using pip install -r requirements.txt

To use ollama, you need to install ollama from [here](https://ollama.com/)

run the following command to install the required model
```bash
ollama run llama3.2-vision:11b-instruct-q8_0
```
## Usage
1. Place your images in the `item` directory. Supported formats are `.jpeg`, `.jpg`, and `.png`.
2. Run the `main.py` script to analyze the images and generate a JSON file:
   ```bash
   python main.py
   ```
3. The output JSON file will be saved as `output/auto_claim.json`.
4. The resulting CSV file will be saved as `output/auto_claim.csv`, and images will be copied to the `output` directory.

## Logging
The application logs information and errors to the console. You can adjust the logging level in the `main.py` file.

## License
This project is licensed under the MIT License.
