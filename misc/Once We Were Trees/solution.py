import os

def ascii_name(name):
    try:
        return chr(int(name))
    except ValueError:
        return name

def print_tree(root, prefix=""):
    entries = sorted([e for e in os.listdir(root) if os.path.isdir(os.path.join(root, e))])
    count = len(entries)

    for i, entry in enumerate(entries):
        path = os.path.join(root, entry)
        connector = "└── " if i == count - 1 else "├── "
        
        print(prefix + connector + ascii_name(entry))
        
        extension = "    " if i == count - 1 else "│   "
        print_tree(path, prefix + extension)

if __name__ == "__main__":
    start_dir = "folders"
    print(ascii_name(os.path.basename(os.path.abspath(start_dir))))
    print_tree(start_dir)
