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
        print(id(notebook))
        [print(str(note)) for note in notebook]

    def create_new_note(self, notebook) -> list:
        print(id(notebook))
        [print(str(note)) for note in notebook]
        title = self.user.prompt('Enter new note title: ')
        text = self.user.prompt('Enter new note text: ')
        new_note = Note(title, text)
        if len(notebook) !=0:
            new_id = max([int(note.id) for note in notebook])+1
        else:
            new_id = 1
        new_note.id = new_id
        notebook.append(new_note)
        print(id(notebook))
        [print(str(note)) for note in notebook]
        return notebook  # list of Note objects

    @staticmethod
    def find_by_id(user_id, notebook) -> None:
        for note in notebook:
            if int(note.id) == int(user_id):
                print(str(note))

    @staticmethod
    def find_by_title(title_contains: str, notebook) -> None:
        notes_found = []
        for note in notebook:
            if str(title_contains) not in str(note.title):
                continue
            else:
                notes_found.append(note)

        if len(notes_found) != 0:
            for note in notes_found:
                print(str(note))
        else:
            print('\nThere is no note containing such text in the title. ')

    def edit_note(self, user_id, notebook):
        # self.notebook = self.db.read_db()
        updated_note = self.user.get_new_note_info()
        title = updated_note[0]
        print(title)
        text = updated_note[1]
        print(text)
        # updated_note = Note(title, text)
        for note in notebook:
            if int(note.id) == int(user_id):
                print(str(note))
                note.title = title
                note.text = text
                print(str(note))
        print(id(notebook))
        [print(str(note)) for note in notebook]
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


# x.show_all_notes()
# print(x.create_new_note())
