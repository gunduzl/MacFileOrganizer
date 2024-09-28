# File Organizer Script

This Python script organizes files in the current directory by grouping them into folders based on their file extensions.

## Features

- Automatically moves files into categories such as Images, Documents, Videos, Music, Archives, Code, and Others.
- Organizes the directory in which the script is run, making file management easier.

## How It Works

1. The script scans the current working directory for all files.
2. Based on the file extensions, it moves each file into a corresponding folder:
   - Images: `.jpg`, `.jpeg`, `.png`, `.gif`, etc.
   - Documents: `.pdf`, `.doc`, `.txt`, etc.
   - Videos: `.mp4`, `.mkv`, etc.
   - Music: `.mp3`, `.wav`, etc.
   - Archives: `.zip`, `.rar`, etc.
   - Code: `.py`, `.js`, `.html`, etc.
   - Others: All unrecognized file types are moved to an "Others" folder.

## Usage

1. Clone this repository or download the script.
2. Place the script in the directory you want to organize.
3. Run the script using the following command in your terminal:

    ```bash
    python3 file_organizer.py
    ```

4. The script will automatically create folders and move files based on their extensions.

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License.
