# Script that removes additionnal null characters (0x00)
# from a file given as command line parameter
# The processed data are saved to a temporary html file.
# That file is then opened by the default application (web browser)
# The target platform is MS Windows
# Usage : python null_remove.py input_file

import os
import sys

def remove_null_characters(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()

    # Remove null characters
    content = content.replace(b'\x00', b'')
    # Replace 0x19 values by 0x27 (')
    content = content.replace(b'\x19', b'\x27')

    return content

def convert_to_utf8(content):
    # Text encodings
    encodings = ['ascii', 'iso-8859-1', 'cp1252']

    for encoding in encodings:
        try:
            decoded_content = content.decode(encoding)
            encoded_content = decoded_content.encode('utf-8')
            return encoded_content
        except UnicodeDecodeError:
            pass

    print("Unable to determine file encoding.")
    sys.exit()

def save_temporary_file(content):
    temp_file_path = '.temp.html'
    with open(temp_file_path, 'wb') as file:
        file.write(content)
    return temp_file_path

def open_with_default_viewer(file_path):
    os.startfile(file_path)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python remove_null_utf8.py <filename>")
        sys.exit()

    file_path = sys.argv[1]

    # Remove null characters from the file
    content = remove_null_characters(file_path)

    # Convert to UTF-8
    content_utf8 = convert_to_utf8(content)

    # Save as a temporary file
    temp_file_path = save_temporary_file(content_utf8)

    # Open with the default viewer
    open_with_default_viewer(temp_file_path)
