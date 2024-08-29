import os
import json
import time


def json_file_exists(file_path):
    """
    Checks if a JSON file exists at the given file path.
    
    Args:
        file_path (str): The path to the JSON file.
        
    Returns:
        bool: True if the file exists, False otherwise.
    """
    # Check if the file exists
    if os.path.isfile(file_path):
        # Check if the file extension is .json
        if file_path.endswith('.json'):
            return True
        else:
            print(f"Warning: {file_path} is not a JSON file.")
            return False
    else:
        return False
    

def _extract_values(data, keys_to_keep, new_key_names):
    keys_2_keep = keys_to_keep[:]
    new_names = new_key_names[:]

    if isinstance(data, dict):
        new_data = {}
        for key, value in data.items():
            if key in keys_2_keep:
                new_key = new_names[keys_2_keep.index(key)]
                new_data[new_key] = value
                new_names.remove(new_names[keys_2_keep.index(key)])
                keys_2_keep.remove(key)
            elif isinstance(value, dict):
                new_data.update(_extract_values(value, keys_2_keep, new_names))
        return new_data


def clean_json_file(file_path, keys_to_keep, new_key_names):
    """
    Creates a new JSON file with only the specified keys from the original file.

    Args:
        file_path (str): The path to the original JSON file.
        keys_to_keep (list): A list of keys to keep in the new file.
        new_key_names (list): A list of new names for the keys in the new file.

    Returns:
        None
    """
    # Open the original file
    file_name = file_path.split('/')[-1].split('.')[0]
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        print(f"\033[92m[+] File {file_name}.json loaded successfully\033[0m")
    except json.JSONDecodeError as e:
        print(f"\033[91m[-] Error decoding {file_name}.json\033[0m")
        print(e)
        return

    # Create a new list of dictionaries with only the desired keys
    new_data = []
    start_time = time.time()
    total_items = len(data)
    processed_items = 0

    for item in data:
        # Extract items
        try:
            new_item = _extract_values(item, keys_to_keep, new_key_names)
            new_data.append(new_item)
            processed_items += 1
            elapsed_time = time.time() - start_time
            remaining_time = int((elapsed_time / processed_items) * (total_items - processed_items))
            countdown_timer = f"Estimated time remaining: {remaining_time // 60:02d}:{remaining_time % 60:02d}"
            print(f"\r{countdown_timer}", end="", flush=True)
        except Exception as e:
            print(f"\033[91m[-] Error: {e}\033[0m")

    print("\n\033[92m[+]Operation completed.\033[0m")

    # Write the new data to a new file
    with open(f'outputs/{file_name}_clean.json', 'w') as new_file:
        json.dump(new_data, new_file, indent=4)
    print(f"\033[92m[+] New file {file_name}_clean.json created successfully and is in your outputs folder\033[0m")

    return
