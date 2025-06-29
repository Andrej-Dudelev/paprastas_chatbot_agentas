import zipfile
import os

# Пути к файлам резюме
files = [
    
]

# Путь к архиву
zip_path = "/mnt/data/Andrej_Dudelev_CV_Package.zip"

# Создание zip-архива
with zipfile.ZipFile(zip_path, 'w') as zipf:
    for file in files:
        zipf.write(file, os.path.basename(file))

zip_path
