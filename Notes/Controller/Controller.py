import time
from Notes.Config import Config
from Notes.View.UserClient import UserClient as user
from Notes.Model.NoteOps import NoteOps as model


class Controller:
    """Class coordinates the work of View and Model"""

    def __init__(self):
        self.notebook = None
        self.model = model()
        self.user = user()
        self.pause = 2

    def run(self):
        # greeting
        self.user.greeting()
        # choose notebook database
        self.notebook = self.model.choose_db()  # str. Path to db file
        # get choice from user
        while True:
            user_action = self.user.show_menu()
            # take action based on choice
            if user_action == 10: return
            match user_action:
                case 1:  # Show all
                    self.model.show_all_notes()
                    time.sleep(self.pause)
                case 2:  # Create
                    self.model.create_new_note()
                    time.sleep(self.pause)
                case 3:
                    break
                case 4:
                    break
                case 5:  # Edit
                    user_id = self.validate_id()
                    self.model.edit_note(user_id)



    def validate_id(self):
        id_valid = False
        while not id_valid:
            try:
                user_id = int(self.user.prompt('Enter id: '))
                if user_id in [int(note.id) for note in self.notebook]:
                    id_valid = True
                else:
                    print('No such id in the notebook. Try again. ')
            except ValueError:
                print('This is not a number. Try again')
        return user_id

# x = Controller()
# x.run()

