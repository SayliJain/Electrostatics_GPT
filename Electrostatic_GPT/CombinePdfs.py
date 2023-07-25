from PyPDF2 import PdfMerger

def combine_pdfs(input_files, output_file):
    merger = PdfMerger()

    for file in input_files:
        merger.append(file)

    merger.write(output_file)
    merger.close()
    print(f"Combined PDFs saved as: {output_file}")

# Example usage
input_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']  # Replace with the input PDF file paths
output_file = 'combined.pdf'  # Replace with the desired output file path

combine_pdfs(input_files, output_file)

