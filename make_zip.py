import zipfile
import os

files_to_include = [
    "Blog",
    "my_site",
    "templates",
    "static",
    "manage.py",
    "Procfile",
    "requirements.txt",
    "db.sqlite3",
    "media",
    ".ebextensions"
]

with zipfile.ZipFile("deploy.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
    for item in files_to_include:
        if os.path.isfile(item):
            zipf.write(item, item)
        elif os.path.isdir(item):
            for root, dirs, files in os.walk(item):
                for file in files:
                    filepath = os.path.join(root, file)

                    # Don't include Python cache files
                    if "__pycache__" in filepath or file.endswith(".pyc"):
                        continue

                    zipf.write(filepath, filepath)

print("deploy.zip created successfully")