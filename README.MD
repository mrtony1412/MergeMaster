
# MergeMaster

**MergeMaster** is a powerful and user-friendly tool to merge files from multiple source folders into a single destination folder.  
It offers filtering options by file type, skipping specific folders, and excluding files by extension.  
MergeMaster also displays a real-time progress bar for better user experience.

---

## ✨ Features

- Merge files from multiple source directories into one destination.
- Filter files by type: images, videos.
- Skip specified folders during the merge.
- Exclude files by their extensions (e.g., `.json`, `.db`).
- Auto-rename files to avoid duplication.
- Display progress with a dynamic progress bar (`tqdm`).
- Show the total number of files successfully merged.

---

## ⚙️ Requirements

- Python >= 3.6
- Third-party libraries:
  - `termcolor`
  - `tqdm`

### Install dependencies:

```bash
pip install termcolor tqdm
```

---

## 🚀 Usage

### Basic Command

```bash
python3 MergeFiles.py [options]
```

---

### Options:

| Argument | Description | Example |
|:-|:-|:-|
| `-f`, `--source_folders` | **(Required)** List of source folders, separated by commas | `/path/to/folder1,/path/to/folder2` |
| `-s`, `--destination_folder` | **(Required)** The target folder where files will be copied | `merged_folder` |
| `-t`, `--types` | Filter by file types (e.g., `image`, `video`) | `image,video` |
| `-k`, `--skip_folders` | Skip specific folder names | `tmp,backup` |
| `-e`, `--exclude_extensions` | Exclude files by extensions (comma-separated) | `.json,.db` |

---

## 🎯 Examples

### Merge only images from two folders:

```bash
python3 MergeFiles.py -t image -f /path1,/path2 -s merged_images
```

### Merge all files except `.json` and `.db` files, skipping specific folders:

```bash
python3 MergeFiles.py -f /path1,/path2 -k cache,tmp -e .json,.db -s merged_output
```

---

## 📦 Output

- All selected files will be merged into the destination folder.
- Duplicate file names are automatically renamed by appending a counter.
- Progress is shown during the copying process.

---

## 📌 Notes

- Make sure the destination folder has sufficient disk space.
- If no `-t` option is provided, **all** files are merged (except those excluded).

---

## 💬 License

This project is released under the MIT License.

---

## 👨‍💻 Author

Made with ❤️ by [Mr.Tony]

- GitHub: [github.com/mr-tony-1412](https://github.com/mr-tony-1412)

---

## 🤝 Contributing

Pull requests are welcome! If you find a bug or have suggestions, feel free to [open an issue](https://github.com/mr-tony-1412/MergeMaster/issues).
