import os

def is_valid_file(file_path):
    """
    Check if the given file path is valid and exists.
    """
    return os.path.isfile(file_path)

def save_to_file(data, output_path):
    """
    Save data to a file in JSON format.
    """
    import json
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)
