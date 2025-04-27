import os
import shutil
import argparse
from termcolor import colored
from tqdm import tqdm

FILE_TYPES = {
    'image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
    'video': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm'],
    'audio': ['.mp3', '.wav', '.aac', '.ogg', '.flac', '.m4a'],
    'document': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
    'archive': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.cs', '.php', '.rb', '.go', '.ts'],
    'ebook': ['.epub', '.mobi', '.azw3', '.fb2']
}

def should_copy(file, types, exclude_extensions, extensions):
    ext = os.path.splitext(file)[1].lower()

    if exclude_extensions and ext in exclude_extensions:
        return False

    if extensions:
        return ext in extensions

    if types:
        for t in types:
            if ext in FILE_TYPES.get(t, []):
                return True

    return not types and not extensions

def collect_files(source_folders, types, skip_keywords, exclude_extensions, extensions):
    files_to_copy = []
    for folder in source_folders:
        for root, dirs, files in os.walk(folder):
            dirs[:] = [d for d in dirs if not any(kw.lower() in d.lower() for kw in skip_keywords)]
            for file in files:
                if should_copy(file, types, exclude_extensions, extensions):
                    files_to_copy.append((root, file, folder))
    return files_to_copy

def merge_files(source_folders, destination_folder, types=None, skip_keywords=None,
                exclude_extensions=None, flat=False, extensions=None):
    print(colored("Starting the file merging process...", 'cyan'))
    os.makedirs(destination_folder, exist_ok=True)

    files_to_copy = collect_files(source_folders, types, skip_keywords, exclude_extensions, extensions)

    with tqdm(total=len(files_to_copy), desc="Merging Files", unit="file") as pbar:
        for root, file, source_root in files_to_copy:
            if flat:
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
        usage="python3 MergeMaster.py -i <input_folders> -o <output_folder> [-t type1,type2] [-x ext1,ext2] [-xe ext1,ext2] [-k keyword1,keyword2] [-F]",
        formatter_class=ColoredHelpFormatter
    )

    parser.add_argument('-i', '--input', type=str, required=True, help="Input folders, separated by commas.")
    parser.add_argument('-o', '--output', type=str, required=True, help="Destination folder.")
    parser.add_argument('-t', '--type', type=str, help="File types to merge (e.g., image,video,document), separated by commas.")
    parser.add_argument('-x', '--ext', type=str, help="Specific file extensions to merge, separated by commas. Example: .png,.jpg")
    parser.add_argument('-xe', '--exclude_ext', type=str, help="File extensions to exclude, separated by commas. Example: .db,.json")
    parser.add_argument('-k', '--skip', type=str, help="Folder name keywords to skip, separated by commas.")
    parser.add_argument('-F', '--flat', action='store_true', help="Copy all files into destination folder without keeping folder structure.")

    args = parser.parse_args()

    source_folders = args.input.split(',')
    types = args.type.split(',') if args.type else None
    skip_keywords = args.skip.split(',') if args.skip else []
    extensions = [ext.lower() if ext.startswith('.') else '.' + ext.lower() for ext in args.ext.split(',')] if args.ext else None
    exclude_extensions = [ext.lower() if ext.startswith('.') else '.' + ext.lower() for ext in args.exclude_ext.split(',')] if args.exclude_ext else None

    merge_files(
        source_folders,
        args.output,
        types=types,
        skip_keywords=skip_keywords,
        exclude_extensions=exclude_extensions,
        flat=args.flat,
        extensions=extensions
    )

if __name__ == "__main__":
    main()
