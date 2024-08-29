# JSON Cleaner

JSON Cleaner is a Python-based command-line tool that allows you to create a new JSON file containing only the desired keys from an existing JSON file. This can be useful when you need to work with a subset of data from a large JSON file or when you want to remove unnecessary keys to reduce file size.

## Features

- Select the keys you want to keep in the new JSON file
- Rename keys in the new JSON file
- Progress tracking with an estimated time remaining display
- Output the cleaned JSON file with indentation for better readability

## Installation

1. Clone the repository:
    
        git clone https://github.com/HawkEyes-OSINT/JsonCleaner.git


2. Navigate to the project directory:

       cd JsonCleaner


3. Install the required dependencies:

        pip install -rrequirements.txt


## Usage

1. Run the `JsonCleaner-terminal.py` script:

        python JsonCleaner-terminal.py


2. Enter the path to your JSON file when prompted.
3. Specify the keys you want to keep in the new file, separated by commas. To rename a key, use the format `key AS new_name, key2, key3 AS new_name2`.
4. The script will create a new JSON file with the specified keys in the `outputs` directory.

