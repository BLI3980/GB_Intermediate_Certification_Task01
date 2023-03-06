import time
from Notes.View.UserClient import UserClient
from Notes.Model.NoteOps import NoteOps


class Controller:
    """Class coordinates the work of View and Model"""

    def __init__(self):
        self.db = None
        self.pause = 2
        self.notebook = []  # Notebook instance to which database will be loaded
        self.model = NoteOps()  # New instance of NoteOps class
        self.user = UserClient()  # New instance of UserClient class

    def run(self):
        # greeting
        self.user.greeting()
        # choose notebook database format
        self.db = self.model.choose_db_type()  # type of database file
        self.notebook = self.db.read_db()  # Load certain type of file into list
        while True:
            # get a choice from user
            user_action = self.user.show_menu()
            # take action based on choice
            if user_action == 7:
                # save to back database
                self.db.save_db(self.notebook)
                return
            match user_action:
                case 1:  # Show all
                    self.user.print_tabulated_table(self.notebook)
                    time.sleep(self.pause)
                case 2:  # Create
                    self.model.create_new_note(self.notebook)
                    time.sleep(self.pause)
                    self.user.confirm(user_action)
                case 3:  # Find by ID
                    user_id = self.validate_id(self.notebook)
                    note_found = self.model.find_by_id(user_id, self.notebook)
                    self.user.print_tabulated_table(note_found)
                    time.sleep(self.pause)
                case 4:  # Find by Title
                    search_title = self.user.prompt('Enter search title: ')
                    notes_found = self.model.find_by_title(search_title, self.notebook)
                    self.user.print_tabulated_table(notes_found)
                    time.sleep(self.pause)
                case 5:  # Edit
                    user_id = self.validate_id(self.notebook)
                    self.model.edit_note(user_id, self.notebook)
                    time.sleep(self.pause)
                    self.user.confirm(user_action)
                case 6:  # Delete
                    user_id = self.validate_id(self.notebook)
                    self.model.delete_note(user_id, self.notebook)
                    time.sleep(self.pause)
                    self.user.confirm(user_action)

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



