import os
import json

def init_repo():
    """
    Initializes a new repository by creating a .gitclone directory with necessary metadata files.
    """
    if not os.path.exists('.gitclone'):
        os.mkdir('.gitclone')
        # Create the structure for storing branches, commits, and HEAD pointer
        os.mkdir('.gitclone/refs')
        os.mkdir('.gitclone/refs/heads')
        os.mkdir('.gitclone/objects')
        with open('.gitclone/HEAD', 'w') as head_file:
            head_file.write('ref: refs/heads/master\n')
        
        # Initial empty index (staging area)
        with open('.gitclone/index', 'w') as index_file:
            index_file.write(json.dumps({}))
        
        print("Initialized empty Git repository in .gitclone/")
    else:
        print("Repository already exists.")

if __name__ == '__main__':
    init_repo()
