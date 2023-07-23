#Install pypdf2
#pip install PyPDF2

import PyPDF2
import os


def extract_text_from_pdf(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

def save_text_to_file(text, output_text_file_path):
    with open(output_text_file_path, 'w', encoding = 'utf-8') as file:
        file.write(text)

# Usage example
# Insert your pdf data file path here
pdf_file_path = "your path name"
os.system(f'start {pdf_file_path}') if os.path.exists(pdf_file_path) else print("File not found.")
# Inser the output text file path here
output_text_file_path = 'your text file name'

text = extract_text_from_pdf(pdf_file_path)
save_text_to_file(text, output_text_file_path)
