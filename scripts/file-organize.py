import os
import shutil
from pathlib import Path

def organize_files(directory):
    """Organize files in a directory by their extensions"""
    
    # Define file type categories and their extensions, but be very careful.
    file_types = {
        "images": [".jpg", ".png", ".gif"],
        "documents": [".pdf", ".docx", ".txt"],
        "audio": [".mp3", ".wav"],
        "videos": [".mp4", ".mov"],
        "archives": [".zip", ".rar"]
    }
    
    # Create folders for each category if they don't exist
    for folder_name in file_types.keys():
        folder_path = Path(directory) / folder_name
        folder_path.mkdir(exist_ok=True)  # Create folder if it doesn't exist
    
    # Scan all files in the directory
    for item in Path(directory).iterdir():
        if item.is_file():  # Only process files, not directories
            file_ext = item.suffix.lower()  # Get file extension
            
            # Find which category this file belongs to
            moved = False
            for category, extensions in file_types.items():
                if file_ext in extensions:
                    dest = Path(directory) / category / item.name
                    shutil.move(str(item), str(dest))  # Move file to category folder
                    print(f"Moved {item.name} to {category}")  # Log action
                    moved = True
                    break
            
            # If file type not categorized, move to 'others'
            if not moved:
                others_path = Path(directory) / "others"
                others_path.mkdir(exist_ok=True)
                shutil.move(str(item), str(others_path / item.name))
                print(f"Moved {item.name} to others")

# Example usage (would need to specify a real directory)
# organize_files("/path/to/your/directory")
