import neovim

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

def _build_task_json(filePath):
    with open(filePath, "w") as file:
        file.write(task_json)
    neovim.command(f"tabedit {filePath}")
    # return filePath

