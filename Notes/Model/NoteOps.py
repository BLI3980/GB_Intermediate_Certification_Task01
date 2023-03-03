from Notes.Config.Config import *
from Notes.Model.DbCsv import DbCsv as db_csv
from Notes.Model.Note import Note
from Notes.View.UserClient import UserClient as user


class NoteOps:
    """Class with all operations with notes"""

    def __init__(self):
        self.db = db_csv()  # ********* Must not be tied to csv format
        self.db_choice = None
        self.userClient = user()

    def choose_db(self) -> str:
        self.db_choice = self.userClient.choose_db_format()
        if self.db_choice == 1:
            source = source_csv
        else:
            source = source_json
        return source

    def show_all_notes(self) -> None:
        all_notes = self.db.read_db()
        self.userClient.print_tabulated_table(all_notes)

    def create_new_note(self) -> list:
        notebook = self.db.read_db()
        title = self.userClient.prompt('Enter new note title: ')
        text = self.userClient.prompt('Enter new note text: ')
        new_note = Note(title, text)
        print(str(new_note))
        notebook.append(new_note)
        return notebook  # list of dictionaries

    def search_note(self):
        pass

    def edit_note(self):
        pass

    def delete_note(self):
        pass


x = NoteOps()
print(x.create_new_note())
