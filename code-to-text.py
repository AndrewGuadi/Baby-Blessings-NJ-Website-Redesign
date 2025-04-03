import os

# Use current working directory as project root
PROJECT_ROOT = os.getcwd()
OUTPUT_FILE = os.path.join(PROJECT_ROOT, "project_snapshot.txt")  # Save output in root

# Define directories and files to skip
EXCLUDED_DIRS = {"instance", "migrations", "__pycache__", "myEnv", ".git"}
EXCLUDED_SUBDIRS = {"/static/images"}  # Skip specific nested directories
EXCLUDED_FILES = {".gitignore", "LICENSE", "code-to-text.py", "project_snapshot.txt", "still_need.txt", "admin-html-suggestions.txt"}

def collect_files(root_dir):
    if not os.path.exists(root_dir):
        print(f"Error: Directory '{root_dir}' does not exist.")
        return []

    collected_data = []
    for root, dirs, files in os.walk(root_dir):
        # Convert full path to relative path
        relative_root = os.path.relpath(root, root_dir)

        # Skip excluded directories
        if any(relative_root.startswith(excluded) for excluded in EXCLUDED_SUBDIRS):
            continue
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        for file in files:
            if file in EXCLUDED_FILES:
                continue  # Skip excluded files

            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, root_dir)

            # Read file content
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                # Format output
                collected_data.append(f"{relative_path}\n```\n{content}\n```\n")
            except Exception as e:
                print(f"Skipping {file_path}: {e}")

    return collected_data

def write_output(data, output_file):
    if not data:
        print("No data collected, skipping write.")
        return

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(data))
    print(f"Project files have been saved to {output_file}")

if __name__ == "__main__":
    files_data = collect_files(PROJECT_ROOT)
    write_output(files_data, OUTPUT_FILE)
