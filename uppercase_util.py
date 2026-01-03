import argparse
import pyperclip
import re

def get_clipboard_text():
    return pyperclip.paste()

def set_clipboard_text(text):
    pyperclip.copy(text)

def to_upper_case(input_string):
    # Remove HTML tags and other hidden characters
    cleaned_string = re.sub(r'<[^<]+?>', '', input_string)
    cleaned_string = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', cleaned_string)
    # Replace newline characters with spaces, except when followed by whitespace
    cleaned_string = re.sub(r'\n(?!\s)', ' ', cleaned_string)
    return cleaned_string.upper()

def main():
    parser = argparse.ArgumentParser(description="Convert input string or clipboard content to uppercase.")
    parser.add_argument("input_string", nargs='?', type=str, help="Input string to convert to uppercase. If not provided, clipboard content will be used.")
    args = parser.parse_args()

    if args.input_string is None:
        clipboard_content = get_clipboard_text()
        output_string = to_upper_case(clipboard_content)
        set_clipboard_text(output_string)
    else:
        output_string = to_upper_case(args.input_string)
        set_clipboard_text(output_string)

    print(output_string)

if __name__ == "__main__":
    main()