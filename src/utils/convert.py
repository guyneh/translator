# Converts a text file to a PDF file with specific formatting

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Spacer

def convert_to_pdf(input_file, output_file):
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read().split('\n')

    # Create a PDF document
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    page_number = 0
    first_page_found = False

    # Process each line
    for line in content:
        line = line.strip()
        if line.isdigit():
            if not first_page_found and line == '1':
                first_page_found = True
            if first_page_found:
                if page_number > 0:
                    story.append(PageBreak())
                page_number += 1
                story.append(Paragraph(f"Page {page_number}", styles['Normal']))
        elif line:
            if first_page_found:
                story.append(Paragraph(line, styles['Normal']))
    
    # Build the PDF
    doc.build(story)

# Use the function
convert_to_pdf('src/data/final.txt', 'src/data/output.pdf')
