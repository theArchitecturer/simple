import os
import os.path
from pathlib import Path

def _find_vscode(filePath):
    if os.path.isfile(filePath):
        filePath, _ = os.path.split(filePath)
    filePathCp = filePath
    while filePath != str(Path.home()):
        for dir in os.listdir(filePath):
            if dir == '.vscode':
                return os.path.join(filePath, dir)
        filePath, _ = os.path.split(filePath)
    return _make_vscode_folder(filePathCp)

def _make_vscode_folder(filePath):
    vscodeDir = os.path.join(filePath, '.vscode')
    try:
        os.mkdir(vscodeDir)
    except FileExistsError:
        pass
    return vscodeDir
