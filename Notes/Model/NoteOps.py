from Notes.Config.Config import *
from Notes.Model.DbCsv import DbCsv as db_csv
from Notes.Model.Note import Note
from Notes.Model.DbManager import DbManager
from Notes.View.UserClient import UserClient as user


class NoteOps:
    """Class with all operations with notes"""

    def __init__(self):
        self.db = None  # ********* Must not be tied to csv format
        self.__db_choice = 0
        self.user = user()
        self.notebook = []
        self.db_manager = DbManager()

    # @property
    # def db_choice(self):
    #     return self.__db_choice
    #
    # # @property
    # # def user(self):
    # #     return self.user
    #
    # @property
    # def notebook(self):
    #     return self.notebook
    #
    # @db_choice.setter
    # def db_choice(self, value):
    #     self.__db_choice = value
    #
    # @notebook.setter
    # def notebook(self, value):
    #     self.notebook = value

    # @user.setter
    # def user(self, value):
    #     self._user = value

    def choose_db(self) -> str:
        self.__db_choice = self.user.choose_db_format()  # int
        if self.__db_choice == 1:
            self.db = self.db_manager.load_csv_db()
            # source = source_csv
        else:
            self.db = self.db_manager.load_json_db()
            # source = source_json
        return self.db.read_db()
        # return source  # str. Path to db file

    def show_all_notes(self) -> None:
        notebook = self.db.read_db()
        [print(str(note)) for note in notebook]

    def create_new_note(self) -> list:
        self.notebook = self.db.read_db()
        title = self.user.prompt('Enter new note title: ')
        text = self.user.prompt('Enter new note text: ')
        new_note = Note(title, text)
        if len(self.notebook) !=0:
            new_id = max([int(note.id) for note in self.notebook])+1
        else:
            new_id = 1
        new_note.id = new_id

        # print(str(new_note))
        self.notebook.append(new_note)
        return self.notebook  # list of dictionaries

    def search_note(self):
        pass

    def edit_note(self, user_id):
        self.notebook = self.db.read_db()
        updated_note = self.user.get_new_note_info()
        title = updated_note[0]
        print(title)
        text = updated_note[1]
        print(text)
        # updated_note = Note(title, text)
        for note in self.notebook:
            if int(note.id) == int(user_id):
                print(str(note))
                note.title = title
                note.text = text
                print(str(note))
        return self.notebook


    def delete_note(self):
        pass


# x.show_all_notes()
# print(x.create_new_note())
