# Processes a text file by removing specific text and formatting

def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove the specified text
    content = content.replace("Here is the English translation of the Hebrew text, preserving all formatting:", "")
    content = content.replace("Here is the translation from Hebrew to English, preserving the formatting:", "")
    content = content.replace("Here is the English translation of the Hebrew text, preserving the formatting:", "")
    content = content.replace("Here is the translation from Hebrew to English, preserving all formatting:", "")
    content = content.replace("Here is the English translation of the Hebrew text, with formatting preserved:", "")
    content = content.replace("Here is the English translation, preserving the formatting:", "")
    content = content.replace("Here is the English translation, preserving all formatting:", "")
    
    # Remove "--- New Page ---"
    content = content.replace("--- New Page ---", "")
    
    # Remove extra blank lines
    content = '\n'.join(line for line in content.splitlines() if line.strip())
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    input_file = "src/data/processed.txt"
    output_file = "src/data/fina.txt"
    process_file(input_file, output_file)
    print(f"Processed file saved as {output_file}")
