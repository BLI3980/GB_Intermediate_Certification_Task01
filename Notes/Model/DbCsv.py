import csv
from Notes.Model.Database import Database
from Notes.Model.Note import Note
from Notes.Config.Config import source_csv


class DbCsv(Database):
    """Class interacts with csv database"""

    def __init__(self):
        super().__init__(source_csv)

    def read_db(self):  # Read from file into a list of Note objects
        notebook = []
        with open(self.database, 'r', encoding='utf-8') as notes:
            for line in notes:
                lst = line.strip().split(';')
                note = Note(lst[1], lst[2])
                note.id = lst[0]
                note.timestamp = lst[3]
                notebook.append(note)
        return notebook

    def save_db(self, notebook):  # From list of Notes write to file
        with open(self.database, 'w', encoding='utf-8', newline='') as db_csv:
            csv_writer = csv.writer(db_csv, delimiter=';')
            for note in notebook:
                csv_writer.writerow([note.id] + [note.title] + [note.text]
                                    + [note.timestamp])
