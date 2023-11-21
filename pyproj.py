import os
import shutil
import argparse

def selective_copy(source_dir, target_dir, extensions):
    for root, _, files in os.walk(source_dir):
        for file in files:
            file_extension = os.path.splitext(file)[1][1:]
            if file_extension in extensions:
                source_path = os.path.join(root, file)
                target_path = os.path.join(target_dir, file)
                shutil.copy2(source_path, target_path)

def main():
    parser = argparse.ArgumentParser(description="Selective Copy Utility")
    parser.add_argument("source_dir", help="Source directory path")
    parser.add_argument("target_dir", help="Target directory path")
    parser.add_argument("extensions", nargs="+", help="List of file extensions to copy")
    args = parser.parse_args()
    source_dir = args.source_dir
    target_dir = args.target_dir
    extensions = args.extensions

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    selective_copy(source_dir, target_dir, extensions)
    print(f"Files with extensions {', '.join(extensions)} copied from {source_dir} to {target_dir}")

if __name__ == "__main__":
    main()
