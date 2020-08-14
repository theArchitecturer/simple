import neovim
import json
import os
from simple.handle_task import _handle_task
from simple.find_vscode import _find_vscode

task_json = """{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "echo",
      "type": "shell",
      "command": "echo hello"
    }
  ]
}
"""

def _make_vscode_folder(filePath):
    vscodeDir = os.path.join(filePath, '.vscode')
    try:
        os.mkdir(vscodeDir)
    except FileExistsError:
        pass
    return vscodeDir

def GetOutput(file):
    with open(file, "r") as outfile:
        data = []
        for line in outfile:
            lineData = json.loads(line)
            group = f'[{lineData["group"]}]'.ljust(10)
            task_name = lineData['task_name']
            data.append(f'{group}{task_name}')
        return data

def _update_jsonl(filePath):
    jsonlFile = os.path.join(filePath, '.task.jsonl') 
    taskFile = os.path.join(filePath, 'task.json')
    _write_jsonl(taskFile, jsonlFile)

def _write_jsonl(taskFile, jsonlFile):
    with open(taskFile, 'r') as inFile:
        with open(jsonlFile, 'w') as outFile:
            tasks = json.load(inFile)['tasks']
            for task in tasks:
                data = dict(_handle_task(task))
                json.dump(data, outFile)
                outFile.write("\n")

def _build_jsonlines(filePath):
    taskFile = os.path.join(filePath, 'task.json')
    jsonlFile = os.path.join(filePath, '.task.jsonl') 
    if not os.path.isfile(taskFile):
        _build_task_json(taskFile)
    _write_jsonl(taskFile, jsonlFile)
    return jsonlFile

def _build_task_json(filePath):
    with open(filePath, "w") as file:
        file.write(task_json)
    neovim.command(f"tabedit {filePath}")
    return filePath


@neovim.plugin
class TestPlugin(object):

    def __init__(self, nvim) -> None:
        self.nvim = nvim
        self.vscodeDir = '' 
        self.task_jsonl = None

    @neovim.autocmd('BufWritePre', pattern='*/.vscode/task.json', eval='expand("%:p:h")')
    def update(self, filePath):
        _update_jsonl(filePath)

    @neovim.autocmd('BufEnter', eval='expand("%:p")')
    def _update_vscodeDir(self, filePath):
        self.vscodeDir = _find_vscode(filePath)

    @neovim.command('Echom')
    def call_build(self):
        if self.task_jsonl == None:
            self.task_jsonl = _build_jsonlines(self.vscodeDir)

        option = [
            '--layout=reverse',
            '-m',
        ]
        opts = {
            'source': GetOutput(os.path.join(self.vscodeDir, '.task.jsonl')),
            'down': '5',
            'option': option
        } 
        self.nvim.call("fzf#run", opts)
