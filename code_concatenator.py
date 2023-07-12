import os
import fnmatch

# File types to be collected
include_file_types = ['*.py', '*.html', '*.css', '*.js', '*.txt', '*.md', '*.ico', '*.png', '*.jpg', '*.jpeg', '*.gif', '*.svg', '*.json']

# File types and directories to be excluded
exclude_file_types = ['files_concatenate.log', 
                      'code_concatenator.py',
                      'README.md',
                      'LICENSE.txt',
                      '*.zip', '*.pyc', '*.log']

exclude_dirs = ['env', '.git', '.vscode', '__pycache__']

def print_files(directory, output_file):
    output_file.write("\nFiles:\n")
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            if any(fnmatch.fnmatch(file, file_type) for file_type in include_file_types) and file not in exclude_file_types:
                output_file.write(f"\nFile: {file_path}\n")
                try:
                    with open(file_path, "r") as file_to_include:
                        output_file.write(file_to_include.read())
                        output_file.write("\n")
                except Exception as e:
                    output_file.write(f"Error reading file: {e}\n")

# Directory to be collected
directory = "."

with open("CodeForReview.log", "w") as output_file:
    print_files(directory, output_file)
