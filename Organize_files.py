#Used to interact with Operating system
import os
#Shell Utilities: Simplify tasks like, Copying, moving, removing etc
import shutil

#Define Categories
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Documents": [".pdf", ".docx", ".xlsx", ".txt", ".pptx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}


# Function to organize files
def organize_files(directory):
    #Get all files in directory
    files = os.listdir(directory)

    for file in files:
        file_path = os.path.join(directory, file)

        #Skip directories
        if os.path.isdir(file_path):
            continue

        #Find the file's extension
        _, ext = os.path.splitext(file)

        for cat, extentions in CATEGORIES.items():
            if ext.lower() in extentions:
                category = cat
                break

        #Create category folder if it doesn't exist
        category_path = os.path.join(directory, category)
        os.makedirs(category_path, exist_ok=True)

        #Move file to category folder
        shutil.move(file_path, os.path.join(category_path, file))

    print("Files are Organized.")


folder_path = input("Enter the path: ")
organize_files(folder_path)
