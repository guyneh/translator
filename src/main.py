# This script translates a PDF document between specified languages using Claude AI and saves the output as a text file.

from PyPDF2 import PdfReader
from clients.llm_clients import claude

# Translates a PDF file between specified languages and saves the result as a text file
def translate_pdf(input_path, output_path, source_lang, target_lang):
    
    # Read the PDF file and initialize a list to store translated pages
    reader = PdfReader(input_path)
    translated_pages = []
    
    for page_num, page in enumerate(reader.pages):
        # Extract text from the current page
        text = page.extract_text()
        
        # Prepare the prompt for translation
        prompt = f"Translate the following text from {source_lang} to {target_lang}, preserving all formatting:\n\n{text}"
        
        # Use Claude AI for translation
        translated_text = claude(prompt, max_tokens=2000, temperature=0.3)
        
        translated_pages.append(translated_text)
        print(f"Translated page {page_num + 1}/{len(reader.pages)}")
        print(f"Translation: {translated_text}")

    # Write all translated pages to a single text file
    with open(output_path, 'w', encoding='utf-8') as f:
        for page in translated_pages:
            f.write(page + "\n\n--- New Page ---\n\n")

    print(f"Translation completed. Output saved to {output_path}")

if __name__ == "__main__":
    # Define input and output file paths
    input_file = "src/data/hebrew.pdf"
    output_file = "src/data/english.txt"
    
    # Execute the translation process
    translate_pdf(input_file, output_file, "Hebrew", "English")