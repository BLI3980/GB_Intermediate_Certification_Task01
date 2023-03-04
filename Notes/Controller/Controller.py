import time
from Notes.View.UserClient import UserClient
from Notes.Model.NoteOps import NoteOps
from Notes.Model.Database import Database


class Controller:
    """Class coordinates the work of View and Model"""

    def __init__(self):
        self.db = None
        self.pause = 2
        self.notebook = []  # Notebook instance to which database will be loaded
        self.model = NoteOps()  # New instance of NoteOps
        self.user = UserClient()  # New instance of UserClient

    def run(self):
        # greeting
        self.user.greeting()
        # choose notebook database
        # self.notebook = self.model.choose_db()
        self.db = self.model.choose_db_type()  # type of database file
        self.notebook = self.db.read_db()  # Load certain type of file
        print(id(self.notebook))
        self.user.print_notebook(self.notebook)
        while True:
            # get a choice from user - integer
            user_action = self.user.show_menu()
            # take action based on choice
            if user_action == 10:
                # save to database
                self.db.save_db(self.notebook)
                return
            match user_action:
                case 1:  # Show all
                    self.model.show_all_notes(self.notebook)
                    time.sleep(self.pause)
                case 2:  # Create
                    self.model.create_new_note(self.notebook)
                    time.sleep(self.pause)
                case 3:  # Find by ID
                    user_id = self.validate_id(self.notebook)
                    self.model.find_by_id(user_id, self.notebook)
                    time.sleep(self.pause)
                case 4:  # Find by Title
                    search_title = self.user.prompt('Enter search title: ')
                    self.model.find_by_title(search_title, self.notebook)
                    time.sleep(self.pause)
                case 5:  # Edit
                    user_id = self.validate_id(self.notebook)
                    self.model.edit_note(user_id, self.notebook)
                    time.sleep(self.pause)
                case 6:  # Delete
                    user_id = self.validate_id(self.notebook)
                    self.model.delete_note(user_id, self.notebook)
                    time.sleep(self.pause)

    def validate_id(self, notebook):
        id_valid = False
        while not id_valid:
            try:
                user_id = int(self.user.prompt('Enter id: '))
                if user_id in [int(note.id) for note in notebook]:
                    id_valid = True
                else:
                    print('No such id in the notebook. Try again. ')
            except ValueError:
                print('This is not a number. Try again')
        return user_id




