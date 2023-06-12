import os
import textract
from datetime import datetime

data_dir = os.path.join(os.curdir, 'data')
pdf_files = ([x for x in os.listdir(data_dir)])

for pdf_file in pdf_files:

    pdf_path = os.path.join(data_dir, pdf_file)
    print(pdf_path)

    text = textract.process(pdf_path, method='pdfminer')

    timestamp_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    with open(f'output/{pdf_file}_{timestamp_str}.txt', 'w') as output_file:
        if isinstance(text, str):
            output_file.write(text)
        else:
            output_file.write(text.decode('utf-8'))
