import os
from pathlib import Path

def _find_vscode(filePath):
    filePathCp = filePath
    while filePath != str(Path.home()):
        filePath, _ = os.path.split(filePath)
        for dir in os.listdir(filePath):
            if dir == '.vscode':
                return os.path.join(filePath, dir)
    return filePathCp
