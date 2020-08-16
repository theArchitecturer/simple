import pytest

import os.path
import os
import pathlib
from simple.dot_vscode import _find_vscode
from simple.build import CommandMacro

class TestDot_vscode:
    def test_find_vscode(self):
        assert _find_vscode('/home/thearchitecturer/Dev/Python/neovim_plugin/simple/rplugin/python3/simple/tests/task.json') == '/home/thearchitecturer/Dev/Python/neovim_plugin/simple/rplugin/python3/simple/tests/.vscode'

class TestBuild:
    def test_command_macro(self):
        command = '${file}'
        obj = CommandMacro(command)
        assert obj.parse_command() == pathlib.Path(__file__).parent.absolute()
