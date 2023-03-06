from datetime import datetime
from Notes.Model.Note import Note
from Notes.Model.DbManager import DbManager
from Notes.View.UserClient import UserClient


class NoteOps:
    """Class with all operations with notes"""

    def __init__(self):
        self.db = None
        self.__db_choice = 0
        self.user = UserClient()
        self.db_manager = DbManager()
        self.notebook = []

    def choose_db_type(self):
        self.__db_choice = self.user.choose_db_format()
        if self.__db_choice == 1:
            self.db = self.db_manager.load_csv_db()
        else:
            self.db = self.db_manager.load_json_db()
        return self.db  # List of Note objects

    @staticmethod
    def show_all_notes(notebook) -> None:
        [print(str(note)) for note in notebook]

    def create_new_note(self, notebook) -> list:
        title = self.user.prompt('Enter new note title: ')
        text = self.user.prompt('Enter new note text: ')
        new_note = Note(title, text)
        if len(notebook) != 0:
            new_id = max([int(note.id) for note in notebook])+1
        else:
            new_id = 1
        new_note.id = new_id
        notebook.append(new_note)
        return notebook  # list of Note objects

    @staticmethod
    def find_by_id(user_id, notebook) -> list:
        note_lst = []
        for note in notebook:
            if int(note.id) == int(user_id):
                note_lst.append(note)
        return note_lst

    @staticmethod
    def find_by_title(title_contains: str, notebook) -> list:
        notes_found = []
        for note in notebook:
            if str(title_contains) not in str(note.title):
                continue
            else:
                notes_found.append(note)

        if len(notes_found) == 0:
            print('\nThere is no note containing such text in the title. ')
            return notes_found
        else:
            return notes_found

    def edit_note(self, user_id, notebook):
        updated_note = self.user.get_new_note_info()
        title = updated_note[0]
        text = updated_note[1]
        for note in notebook:
            if int(note.id) == int(user_id):
                note.title = title
                note.text = text
                note.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return notebook

    @staticmethod
    def delete_note(user_id, notebook):
        list_index = 0
        target_index = 0
        for note in notebook:
            if int(note.id) == int(user_id):
                target_index = list_index
            list_index += 1
        notebook.pop(target_index)

