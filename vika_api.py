from vika import Vika
from config import config
config = config()

vika = Vika(config['vika']['token'])

datasheet = vika.datasheet(config['vika']['datasheet'], field_key="name")


def insert(title, project, root, id):
    row = datasheet.records.create({
        "title": title,
        "project": project,
        "root": root,
        "id": id
    })
    records = datasheet.records.all()
    for record in records:
        print(record.json())


def insert_relax():
    row = datasheet.records.create({
        "title": "relax",
        "project": '',
        "root": '',
        "id": 0
    })
    records = datasheet.records.all()
    for record in records:
        print(record.json())
