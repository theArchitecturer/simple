import neovim

class HandleKey():
    def __init__(self):
        self.task = []

    def _handle_label(self, key):
        return self.task[key]

    def _handle_group(self, key):
        return self.task[key]

    def _handle_task(self, task) -> dict:
        # self.task = task
        # keyToCheck = ['label', 'group']
        # toReturn = {}

        # for key in keyToCheck:
        #     pass
            # toReturn[key] = getattr(HandleKey, f'_handle_{key}')(self, key)
        obj = CommandMacro('${file}')
        print(obj.parse_command())


class CommandMacro():

    def __init__(self, command):
        self.command = command

    @staticmethod
    def _handle_file():
        return neovim.eval('expand("%:p")')

    # def 

    def parse_command(self):
        begin_brace = None
        end_brace = None
        _return = ''
        i=0
        while i != len(self.command):
            if self.command[i] == '$':
                if self.command[i+1] == '$':
                    _return = f'{_return}$'
                elif self.command[i+1] == '{':
                    begin_brace = i
            elif self.command[i] == '}':
                if begin_brace is None:
                    neovim.command('invalid macro')
                else:
                    return_macro = getattr(CommandMacro, f'_handle_{self.command[begin_brace:end_brace]}')
                    _return = f'{_return}{return_macro}'
        return _return
