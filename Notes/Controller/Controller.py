from Notes.Config import Config
from Notes.View.UserClient import UserClient as user
from Notes.Model.NoteOps import NoteOps as model


class Controller:
    """Class coordinates the work of View and Model"""

    def __init__(self):
        self.notebook = None
        self.model = model()
        self.user = user()

    def run(self):
        # greeting
        self.user.greeting()
        # choose notebook database
        self.notebook = self.model.choose_db()
        # get choice from user
        while True:
            user_action = self.user.show_menu()
            # take action based on choice
            if user_action == 10: return
            match user_action:
                case 1:  # Show all notes
                    self.model.show_all_notes()
                    break
                case 2:  # Create new note
                    self.model.create_new_note(self.notebook)
                    # if
                    break
                case 3:
                    break
                case 4:
                    break
                case 5:
                    break
            # choice = self.interact.show_menu()


# x = Controller()
# x.run()

