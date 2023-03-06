import json
from Notes.Model.Database import Database
from Notes.Model.Note import Note
from Notes.Config.Config import source_json


class DbJson(Database):
    """Class interacts with csv database"""
    def __init__(self):
        super().__init__(source_json)

    def read_db(self):  # Read from file into list of Note instances
        notebook = []
        with open(self.database, 'r', encoding='utf-8') as json_file:
            for line in json_file:
                lst = json.loads(line.strip())
                note = Note(lst['title'], lst['text'])
                note.id = int(lst['_Note__id'])
                note.timestamp = lst['timestamp']
                notebook.append(note)
        return notebook

    def save_db(self, notebook):  # From list of Notes write to file
        with open(self.database, 'w', encoding='utf-8', newline='') as db_json:
            for note in notebook:
                temp = json.dumps(note.__dict__)
                db_json.write(temp)
                db_json.write('\n')

