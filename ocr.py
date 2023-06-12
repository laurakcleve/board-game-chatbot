import os
import pytesseract
from datetime import datetime

if __name__ == "__main__":
    input_dir = os.path.join(os.curdir, 'data/pdf2image_output')
    output_dir = os.path.join(os.curdir, 'data/ocr_output')

    image_files = sorted([x for x in os.listdir(input_dir)])

    for image_file in image_files:

        image_path = os.path.join(input_dir, image_file)
        print(image_path)

        text = pytesseract.image_to_string(image_path)

        timestamp_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        with open(f'{output_dir}/{image_file}_{timestamp_str}.txt', 'w') as output_file:
            output_file.write(text)
