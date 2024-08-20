import argparse
from repo import init_repo
from index import add_file_to_index, add_all_files_to_index
from commit import create_commit
from branch import create_branch, checkout_branch

def main():
    parser = argparse.ArgumentParser(description="Git-clone, a simple Git clone.")
    subparsers = parser.add_subparsers(dest='command')

    # Init command
    subparsers.add_parser('init')

    # Add command
    parser_add = subparsers.add_parser('add')
    parser_add.add_argument('file', nargs='?', default=None)  # Optional file argument
    parser_add.add_argument('--all', action='store_true')  # Add --all flag

    # Commit command
    parser_commit = subparsers.add_parser('commit')
    parser_commit.add_argument('-m', '--message', required=True)

    # Branch command
    parser_branch = subparsers.add_parser('branch')
    parser_branch.add_argument('branch_name')

    # Checkout command
    parser_checkout = subparsers.add_parser('checkout')
    parser_checkout.add_argument('branch_name')

    args = parser.parse_args()

    if args.command == 'init':
        init_repo()
    elif args.command == 'add':
        if args.all:
            add_all_files_to_index()
        else:
            add_file_to_index(args.file)
    elif args.command == 'commit':
        create_commit(args.message)
    elif args.command == 'branch':
        create_branch(args.branch_name)
    elif args.command == 'checkout':
        checkout_branch(args.branch_name)

if __name__ == '__main__':
    main()
