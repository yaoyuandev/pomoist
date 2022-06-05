from pathlib import Path
import json


def config():
    home = str(Path.home())
    return json.load(open(f'{home}/.pomoist.json'))
