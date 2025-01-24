from PyPDF2 import PdfReader

file_path = './images/AGED.pdf'

def read_files(file_path):
    try:
        reader = PdfReader(file_path)

        with open("invitation.txt", "w") as output_file:
            for page in reader.pages:
                text = page.extract_text()
                if text:  # Ensure there's text to write
                    output_file.write(text )
        return f"File read successfully"
        
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return None
    except PermissionError as e:
        print(f"Permission denied: {e}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

print(read_files(file_path))

