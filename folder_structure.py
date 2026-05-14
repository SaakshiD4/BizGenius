# save as print_structure.py
# Run inside project folder:
# python print_structure.py

import os

root_dir = os.getcwd()

# Folders to ignore
ignore_dirs = {
    "node_modules",
    "venv",
    ".venv",
    "env",
    "__pycache__",
    ".git",
    "dist",
    "build",
    ".next",
    ".idea",
    ".vscode",
    "target",
    "coverage"
}

# Files to ignore
ignore_files = {
    ".DS_Store",
    "package-lock.json",
    "yarn.lock"
}


def should_ignore(name):
    return name in ignore_dirs or name in ignore_files


def print_tree(directory, prefix=""):
    try:
        items = sorted(os.listdir(directory))
    except PermissionError:
        return

    items = [item for item in items if not should_ignore(item)]

    for index, item in enumerate(items):
        full_path = os.path.join(directory, item)
        is_last = index == len(items) - 1
        symbol = "└── " if is_last else "├── "

        print(prefix + symbol + item)

        if os.path.isdir(full_path):
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(full_path, new_prefix)


print("\nProject Structure:\n")
print(os.path.basename(root_dir))
print_tree(root_dir)