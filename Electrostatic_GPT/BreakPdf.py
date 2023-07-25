from PyPDF2 import PdfReader, PdfWriter

def break_pdf(input_path, output_path, start_page, end_page):
    with open(input_path, 'rb') as file:
        pdf = PdfReader(file)
        total_pages = len(pdf.pages)
        
        if start_page < 1 or start_page > total_pages:
            print(f"Invalid start page number. Total pages: {total_pages}")
            return
        if end_page > total_pages or end_page < start_page:
            print(f"Invalid end page number. Total pages: {total_pages}")
            return

        writer = PdfWriter()
        for page_num in range(start_page - 1, end_page):
            writer.add_page(pdf.pages[page_num])

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

        print(f"PDF successfully broken from page {start_page} to {end_page}. Output saved as: {output_path}")

# Example usage
input_file = "./JEEAdv2023_Paper2.pdf"  # Replace with your input PDF file path
output_file = "JEE_Advance_2023_paper2_physics_Doubt_Questions.pdf"  # Replace with the desired output file path
start_page = 20  # Replace with the desired start page number
end_page = 21  # Replace with the desired end page number

break_pdf(input_file, output_file, start_page, end_page)