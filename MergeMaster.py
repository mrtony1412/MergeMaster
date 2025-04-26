import os
import shutil
import argparse
from termcolor import colored
from tqdm import tqdm  # Thêm import tqdm

FILE_TYPES = {
    'image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
    'video': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm']
}

def should_copy(file, types, exclude_extensions):
    ext = os.path.splitext(file)[1].lower()
    
    if exclude_extensions and ext in exclude_extensions:
        return False

    if not types:
        return True

    for t in types:
        if ext in FILE_TYPES.get(t, []):
            return True
    return False

def collect_files(source_folders, types, skip_folders, exclude_extensions):
    files_to_copy = []

    for folder in source_folders:
        for root, dirs, files in os.walk(folder):
            dirs[:] = [d for d in dirs if d not in skip_folders]
            for file in files:
                if should_copy(file, types, exclude_extensions):
                    files_to_copy.append((root, file, folder))
    return files_to_copy

def merge_files(source_folders, destination_folder, types=None, skip_folders=None, exclude_extensions=None):
    print(colored("Starting the file merging process...", 'cyan'))
    os.makedirs(destination_folder, exist_ok=True)

    files_to_copy = collect_files(source_folders, types, skip_folders, exclude_extensions)

    with tqdm(total=len(files_to_copy), desc="Merging Files", unit="file") as pbar:
        for root, file, source_root in files_to_copy:
            if types:
                dest_path = destination_folder
            else:
                relative_path = os.path.relpath(root, source_root)
                dest_path = os.path.join(destination_folder, relative_path)
                os.makedirs(dest_path, exist_ok=True)

            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_path, file)

            base, ext = os.path.splitext(file)
            counter = 1
            while os.path.exists(dest_file):
                new_name = f"{base}_{counter}{ext}"
                dest_file = os.path.join(dest_path, new_name)
                counter += 1

            shutil.copy2(src_file, dest_file)
            pbar.update(1)

    print(colored(f"Merging {len(files_to_copy)} files completed successfully!", 'green'))

class ColoredHelpFormatter(argparse.HelpFormatter):
    def _format_usage(self, usage, actions, groups, prefix):
        usage = colored(usage, 'cyan')
        return super()._format_usage(usage, actions, groups, prefix)

    def _format_action_invocation(self, action):
        result = super()._format_action_invocation(action)
        if action.option_strings:
            return colored(result, 'green')
        return result

    def _format_option_string(self, action):
        return colored(action.option_strings[0], 'blue')

    def _format_description(self, description):
        if description:
            return colored(description, 'yellow')
        return description

def main():
    parser = argparse.ArgumentParser(
        prog="MergeMaster",
        description="Merge files from multiple source folders into a destination folder.",
        usage="python3 MergeMaster.py [-t type1,type2] [-k folder1,folder2] [-e .ext1,.ext2] -f <source_folders> -s <destination_folder>",
        formatter_class=ColoredHelpFormatter
    )

    parser.add_argument('-t', '--types', type=str, help="File types to merge (e.g., image,video), separated by commas.")
    parser.add_argument('-k', '--skip_folders', type=str, help="Folder names to skip, separated by commas.")
    parser.add_argument('-e', '--exclude_extensions', type=str, help="File extensions to exclude, separated by commas. Example: .json,.db")
    parser.add_argument('-f', '--source_folders', type=str, required=True, help="List of source folders, separated by commas.")
    parser.add_argument('-s', '--destination_folder', type=str, required=True, help="Destination folder where the files will be copied.")

    args = parser.parse_args()

    source_folders = args.source_folders.split(',')
    types = args.types.split(',') if args.types else None
    skip_folders = args.skip_folders.split(',') if args.skip_folders else []
    exclude_extensions = [ext.lower() for ext in args.exclude_extensions.split(',')] if args.exclude_extensions else None

    merge_files(source_folders, args.destination_folder, types, skip_folders, exclude_extensions)

if __name__ == "__main__":
    main()
