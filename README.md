# Uppercase Utility

[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](https://github.com/voothi/20240824103911-uppercase-util)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight utility for converting text to uppercase, cleaning up HTML tags, and normalizing spacing from the clipboard or terminal.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Building from Source](#building-from-source)
- [AHKv2 Integration](#ahkv2-integration)
- [License](#license)

---

## Description
`uppercase-util` is a focused tool that processes text to ensure it is in uppercase and free from unwanted formatting characters. It is particularly useful when preparing text for documents, headers, or any context requiring consistent uppercase format.

[Return to Top](#uppercase-utility)

## Features
- **Uppercase Conversion**: Automatically converts all input text to uppercase.
- **HTML Cleanup**: Removes HTML tags and special entities.
- **Control Character Removal**: Strips non-printable and control characters.
- **Newline Normalization**: Joins single lines while preserving paragraph breaks (newlines followed by whitespace).
- **Clipboard Integration**: Seamlessly reads from and writes back to the system clipboard.

[Return to Top](#uppercase-utility)

## Installation

### Using Python (Primary Method)
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install pyperclip
   ```
3. Run the script:
   ```bash
   python uppercase_util.py
   ```

[Return to Top](#uppercase-utility)

## Usage

1. **Option A (Clipboard)**: Copy text to your clipboard and run the script without arguments:
   ```powershell
   python uppercase_util.py
   ```
   The cleaned text will be written back to your clipboard.

2. **Option B (Command Line)**: Pass the text as a command line argument:
   ```powershell
   python uppercase_util.py "text to convert"
   ```

[Return to Top](#uppercase-utility)

## Building from Source

For a standalone executable, you can use PyInstaller:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller==5.13.2
   ```
2. Build the executable:
   ```bash
   pyinstaller --onefile --noconsole uppercase_util.py
   ```
The executable will be located in the `dist/` directory.

[Return to Top](#uppercase-utility)

## AHKv2 Integration

For a more seamless workflow, you can use the **[uppercase.ahk](https://github.com/voothi/20240411110510-autohotkey/blob/main/uppercase.ahk)** script.

[Return to Top](#uppercase-utility)

## License
MIT License. See LICENSE file for details.

[Return to Top](#uppercase-utility)
