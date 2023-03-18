import argparse
import PyPDF2

# calling template
# python <script_name>.py -i <input filename> -o <output filename>
# calling example
# python pdf2text.py -i input.pdf -o output.txt


def pdf_to_text(input_file, output_file):
    with open(input_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        text = ''
        for page in range(pdf_reader.getNumPages()):
            page_obj = pdf_reader.getPage(page)
            text += page_obj.extractText()
    
    with open(output_file, 'w') as f:
        f.write(text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert PDF to raw text')
    parser.add_argument('-i', '--input', help='Input PDF filename', required=True)
    parser.add_argument('-o', '--output', help='Output text filename', required=True)
    args = parser.parse_args()

    pdf_to_text(args.input, args.output)
