import os

def path_normalizer(path):
    '''Path resolver for different OS'''

    if not path:
        print('Path not provided')
        return
    return os.path.normpath(path)
