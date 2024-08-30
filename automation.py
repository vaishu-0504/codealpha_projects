import os
import shutil

source_dir = "C:\\Users\\vaish\\Desktop\\MyOrganizedFiles"
if not os.path.exists(source_dir):
    os.makedirs(source_dir)
    print(f"The directory {source_dir} was not found, so it has been created.")

dest_dirs = {
    'images': 'Images',
    'documents': 'Documents',
    'music': 'Music',
    'videos': 'Videos',
}

extensions = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'music': ['.mp3', '.wav', '.aac'],
    'videos': ['.mp4', '.mkv', '.mov', '.avi'],
}

def organize_files():
    for root, dirs, files in os.walk(source_dir):
        for filename in files:
            file_ext = os.path.splitext(filename)[1].lower()
            for category, ext_list in extensions.items():
                if file_ext in ext_list:
                    dest_dir = os.path.join(source_dir, dest_dirs[category])
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)
                    shutil.move(os.path.join(root, filename), os.path.join(dest_dir, filename))
                    print(f"Moved: {filename} to {dest_dir}")
                    break

if __name__ == "__main__":
    organize_files()
