def _handle_task(task) -> dict:
    keyToCheck = ['label', 'group']
    toReturn = {}

    for key in keyToCheck:
        toReturn[key] = getattr(HandleKey, f'_handle_{key}', [ key, task ])

    return toReturn

class HandleKey():
    @staticmethod
    def _handle_label(key, task):
        return task[f'{key}']

    def _handle_group(key, task):
        return task[f'{key}']
