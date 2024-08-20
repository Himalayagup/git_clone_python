import os

def create_branch(branch_name):
    """Create a new branch by copying the HEAD of the current branch."""
    if not os.path.exists('.gitclone'):
        print("Error: No Git repository initialized.")
        return

    with open('.gitclone/HEAD', 'r') as head_file:
        current_branch = head_file.read().strip().split(' ')[-1]

    with open(f'.gitclone/{current_branch}', 'r') as branch_file:
        commit_hash = branch_file.read().strip()
    
    # Create a new branch that points to the same commit
    with open(f'.gitclone/refs/heads/{branch_name}', 'w') as new_branch:
        new_branch.write(commit_hash)
    
    print(f"Branch {branch_name} created.")

def checkout_branch(branch_name):
    """Switch to a different branch by updating HEAD."""
    if not os.path.exists(f'.gitclone/refs/heads/{branch_name}'):
        print(f"Error: Branch {branch_name} does not exist.")
        return
    
    # Update HEAD to point to the new branch
    with open('.gitclone/HEAD', 'w') as head_file:
        head_file.write(f'ref: refs/heads/{branch_name}\n')

    print(f"Switched to branch {branch_name}.")

if __name__ == '__main__':
    create_branch('new-feature')
