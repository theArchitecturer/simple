import neovim
import json
import os
import simple.dot_vscode
import simple.task_json
import simple.handle_task

@neovim.plugin
class Simple(object):

    def __init__(self, nvim) -> None:
        self.nvim = nvim
        self.vscodeDir = None
        self.taskFile = None

    # @neovim.autocmd('BufEnter', eval='expand("%:p")')
    # def _initialize_vscodeDir(self, filePath):

    @neovim.command('Echom', eval='expand("%:p")')
    def call_build(self, filePath):
        if self.vscodeDir is None:
            self.vscodeDir = simple.dot_vscode._find_vscode(filePath)
        if self.taskFile is None:
            self.taskFile = os.path.join(self.vscodeDir, 'task.json')
        if os.path.isfile(self.taskFile):
            pass
        else:
            simple.task_json._build_task_json(self.taskFile)
    #     self.nvim.call("fzf#run", simple.fzf.opts)
    # @neovim.command('Echomm')
    # def print_file(self):
    #     file = simple.handle_task.CommandMacro()._handle_file()
    #     self.nvim.command(f'echo {file}')
