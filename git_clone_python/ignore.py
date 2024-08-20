def is_ignored(file_path):
    """Check if the file is ignored based on the .gitcloneignore file."""
    if not os.path.exists('.gitcloneignore'):
        return False
    
    with open('.gitcloneignore', 'r') as ignore_file:
        ignored_patterns = ignore_file.read().splitlines()

    for pattern in ignored_patterns:
        if file_path.startswith(pattern):
            return True
    return False
