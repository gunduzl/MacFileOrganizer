import os
import shutil

# Get the current working directory (where the script is located)
current_folder = os.getcwd()

# Match folder names with extensions to group files by their types
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.wmv'],
    'Music': ['.mp3', '.wav', '.flac', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp'],
    'Others': []  # Other files
}

# Move files to the appropriate folder based on their extension
def organize_folder():
    for item in os.listdir(current_folder):
        item_path = os.path.join(current_folder, item)

        # If it's a file, get the extension
        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item)

            # Find out which folder to move the file to
            moved = False
            for folder, extensions in file_types.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(current_folder, folder)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    shutil.move(item_path, os.path.join(target_folder, item))
                    moved = True
                    break

            # If the file extension is not recognized, move it to the Others folder
            if not moved:
                others_folder = os.path.join(current_folder, 'Others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(item_path, os.path.join(others_folder, item))

if __name__ == "__main__":
    organize_folder()
    print("Files successfully grouped by their extensions!")
