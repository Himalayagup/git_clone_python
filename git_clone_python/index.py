import os
import hashlib
import json

def hash_file(file_path):
    """Hash a file to detect changes."""
    hasher = hashlib.sha1()
    with open(file_path, 'rb') as f:
        buffer = f.read()
        hasher.update(buffer)
    return hasher.hexdigest()

def add_file_to_index(file_path):
    """Add a single file to the staging area (index)."""
    if not file_path or not os.path.exists(file_path):
        print(f"Error: {file_path} does not exist.")
        return
    
    if not os.path.exists('.gitclone'):
        print("Error: No Git repository initialized.")
        return

    # Load the current index
    with open('.gitclone/index', 'r') as index_file:
        index = json.load(index_file)

    # Hash the file and add to index
    file_hash = hash_file(file_path)
    index[file_path] = file_hash

    # Save the updated index
    with open('.gitclone/index', 'w') as index_file:
        json.dump(index, index_file, indent=4)
    
    print(f"Added {file_path} to the staging area.")

def add_all_files_to_index():
    """Add all files in the current directory to the staging area (index)."""
    if not os.path.exists('.gitclone'):
        print("Error: No Git repository initialized.")
        return
    
    # Load the current index
    with open('.gitclone/index', 'r') as index_file:
        index = json.load(index_file)

    # Add all files in the directory to the index
    for root, dirs, files in os.walk('.'):
        for file_name in files:
            if not file_name.startswith('.gitclone'):  # Ignore the .gitclone directory
                file_path = os.path.join(root, file_name)
                file_hash = hash_file(file_path)
                index[file_path] = file_hash
                print(f"Added {file_path} to the staging area.")

    # Save the updated index
    with open('.gitclone/index', 'w') as index_file:
        json.dump(index, index_file, indent=4)

if __name__ == '__main__':
    add_all_files_to_index()
