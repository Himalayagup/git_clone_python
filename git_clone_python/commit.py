import os
import json
import hashlib
from datetime import datetime

def create_commit(message):
    """Create a commit with the staged files."""
    if not os.path.exists('.gitclone'):
        print("Error: No Git repository initialized.")
        return

    # Load the current index (staging area)
    with open('.gitclone/index', 'r') as index_file:
        index = json.load(index_file)
    
    if not index:
        print("Nothing to commit.")
        return
    
    # Generate commit object and store it in the .gitclone/objects directory
    commit_content = {
        'message': message,
        'timestamp': str(datetime.now()),
        'files': index,
    }
    commit_hash = hashlib.sha1(json.dumps(commit_content).encode()).hexdigest()

    with open(f'.gitclone/objects/{commit_hash}', 'w') as commit_file:
        json.dump(commit_content, commit_file, indent=4)
    
    print(f"Committed: {message}")
    
    # Clear the staging area after commit
    with open('.gitclone/index', 'w') as index_file:
        json.dump({}, index_file, indent=4)
    
    # Update the branch reference (HEAD -> master)
    with open('.gitclone/HEAD', 'r') as head_file:
        head_ref = head_file.read().strip().split(' ')[-1]
    
    with open(f'.gitclone/{head_ref}', 'w') as branch_file:
        branch_file.write(commit_hash)

if __name__ == '__main__':
    create_commit('Initial commit')
