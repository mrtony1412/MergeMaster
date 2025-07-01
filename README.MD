
# 📂 MergeMaster

**MergeMaster** is a powerful command-line tool that helps you **merge files from multiple folders** into a single destination folder.  
You can **keep** or **flatten** the folder structure, **filter files** by type or extension, and **skip folders** based on keywords.

---

## 🚀 Features

- Copy files by **specific extensions** (e.g., `.jpg`, `.png`, `.mp4`).
- Filter files by **file type** (`image`, `video`, `document`).
- **Skip folders** containing specific keywords (e.g., `stickers`, `backup`, `temp`).
- Option to **keep folder structure** or **flatten** into a single directory.
- Automatically **rename** files to avoid overwriting.
- Progress bar with **tqdm**.
- Simple and colored command-line interface.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/mr-tony-1412/MergeMaster.git
cd MergeMaster
pip install -r requirements.txt
```

**Requirements**:
- Python 3.6+
- tqdm
- termcolor

---

## ⚙️ Usage

Basic syntax:

```bash
python3 MergeMaster.py -i <input_folders> -o <output_folder> [options]
```

### 🔥 Main options:

| Option | Description |
| :--- | :--- |
| `-i`, `--input` | **(Required)** Input folders, separated by commas. |
| `-o`, `--output` | **(Required)** Destination folder. |
| `-t`, `--type` | File types to merge: `image`, `video` (separated by commas). |
| `-x`, `--ext` | Specific extensions to merge (e.g., `.jpg,.png`). |
| `-xe`, `--exclude_ext` | Extensions to exclude (e.g., `.db,.json`). |
| `-k`, `--skip` | Folder name keywords to skip (e.g., `stickers,backup`). |
| `-F`, `--flat` | Flatten all files into the destination folder without keeping folder structure. |

---

### 📋 Examples

✅ Merge `.jpg` and `.png` files, flatten folder structure:

```bash
python3 MergeMaster.py -i /path/to/folder1,/path/to/folder2 -o /path/to/output -x jpg,png -F
```

✅ Merge only image files, keeping folder structure:

```bash
python3 MergeMaster.py -i /path/to/photos -o /path/to/merged_photos -t image
```

✅ Merge videos, exclude `.mkv` files, and skip folders containing `backup`:

```bash
python3 MergeMaster.py -i /videos -o /merged_videos -t video -xe .mkv -k backup
```

---

## 👨‍💻 Author

Made with ❤️ by [Mr.Tony]

- GitHub: [github.com/mrtony1412](https://github.com/mrtony1412)

---

## 🤝 Contributing

Pull requests are welcome!  
If you find a bug or have suggestions, feel free to [open an issue](https://github.com/mrtony1412/MergeMaster/issues).

---

## 📜 License

This project is licensed under the MIT License.
