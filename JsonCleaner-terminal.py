import pyfiglet
import backend

def display_json_cleaner_ascii():
    """
    Prints the JSON Cleaner ASCII art using the pyfiglet library.
    This function is called when the program starts to introduce the user to the tool.
    """
    font = pyfiglet.Figlet(font='slant')
    ascii_art = font.renderText('JsonCleaner')
    print(ascii_art)


def get_json_file_path():
    """
    Prompts the user to enter the path to a JSON file.
    Validates the input and checks if the file exists.
    Returns the path to the JSON file if it exists.
    """
    display_json_cleaner_ascii()
    while True:
        json_file = input("Enter the path to your JSON file: ")
        file_name = json_file.split('/')[-1]

        # check if json file
        if not json_file.endswith('.json'):
            print("\033[91m[-] Not a JSON file\033[0m")
            continue

        # check if file exists
        if backend.json_file_exists(json_file):
            print(f"\033[92m[+] File {file_name} found\033[0m")
            return json_file
        else:
            print(f"\033[91m[-] Could not locate file {file_name}, please check the path and try again\033[0m")


def get_key_mapping():
    """
    Receive a list of keys to keep in the JSON file.
    Print a table of the original and new key names.
    Returns the original and new key lists.
    :return: list, list
    """
    # provide instructions
    print("Enter the JSON keys you want to keep, separated by commas")
    print("To provide a new name for a key, use the format 'key AS new_name")
    print("Example: key1 AS new_key1, key2 AS new_key2")
    
    # get input of keys
    user_input = input("Enter the keys: ")
    keys = user_input.split(',')
    original_keys = []
    new_keys = []

    # create orginal and new key lists
    for key in keys:
        key = key.strip()
        if ' AS ' in key:
            original_keys.append(key.split(' AS ')[0])
            new_keys.append(key.split(' AS ')[1])
        else:
            original_keys.append(key)
            new_keys.append(key)

    # print the key lists as table
    print("\nKeys to Keep\tNew Key Name")
    print("--------------\t---------")
    for orig, new in zip(original_keys, new_keys):
        print(f"{orig}\t\t{new}")
    print()

    return original_keys, new_keys


def main():
    """
    Main function to run the JSON Cleaner program.
    """
    json_file = get_json_file_path()
    original_keys, new_keys = get_key_mapping()
    backend.clean_json_file(json_file, original_keys, new_keys)
    

if __name__ == '__main__':
    main()