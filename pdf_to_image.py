import os
import pdf2image

if __name__ == "__main__":

    input_dir = os.path.join(os.curdir, 'data/pdf2image_input')
    output_dir = os.path.join(os.curdir, 'data/pdf2image_output')

    pdf_files = ([x for x in os.listdir(input_dir)])

    for pdf_file in pdf_files:

        pdf_path = os.path.join(input_dir, pdf_file)
        print(pdf_path)

        images = pdf2image.convert_from_path(pdf_path)

        for i, image in enumerate(images):
            image.save(f'{output_dir}/image{str(i+1).zfill(2)}.png', 'PNG')
