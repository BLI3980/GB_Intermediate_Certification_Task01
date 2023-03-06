from tabulate import tabulate
from emoji import emojize


class UserClient:
    """Class gets information from user"""
    def __init__(self):
        self.is_ok = None

    @staticmethod
    def greeting():
        return print('\nWelcome to notebook app!')

    @staticmethod
    def confirm(operation) -> None:
        if operation == 2:
            return print('\nNew note successfully created.\n')
        if operation == 5:
            return print('\nThe note successfully updated.\n')
        if operation == 6:
            return print('\nThe note is now deleted.\n')

    def choose_db_format(self) -> int:
        print('\nWhich database format do you want to use?')
        self.is_ok = False
        while not self.is_ok:
            try:
                select = int(input('Choose "1" for .csv or "2" for .json: '))
                self.is_ok = True
                if select not in [1, 2]:
                    self.is_ok = False
                    print('Incorrect number. Try again. ')
            except ValueError:
                print('This is not a number. Try again. ')
        return select  # Choice number

    def show_menu(self) -> int:
        print("\nChoose an action from the list below: ")
        print("=" * 35)
        print(emojize("1. :notebook: Show the entire notebook"))
        print(emojize("2. :NEW_button: Create new note"))
        print(emojize("3. :magnifying_glass_tilted_left: Find a note by ID"))
        print(emojize("4. :magnifying_glass_tilted_right: Find a note by Title"))
        print(emojize("5. :memo: Edit a note"))
        print(emojize("6. :cross_mark: Delete a note"))
        print(emojize("7. :stop_button:End the work"))
        print("=" * 35 + "\n")
        self.is_ok = False
        while not self.is_ok:
            try:
                select = int(input("Enter a number of corresponding action: "))
                self.is_ok = True
                if select not in range(1, 8):
                    self.is_ok = False
                    print('Incorrect number. Try again.')
            except ValueError:
                print('This is not a number. Try again.')
        return select

    def get_new_note_info(self) -> tuple:
        title = self.prompt('Enter the title for the note: ')
        text = self.prompt('Enter the details of the note: ')
        return title, text

    @staticmethod
    def print_tabulated_table(list_of_notes) -> None:
        table = []
        note_lst = []
        for note in list_of_notes:
            note_lst.append(note.id)
            note_lst.append(note.title)
            note_lst.append(note.text)
            note_lst.append(note.timestamp)
            # Get a list of lists.
            table.append(note_lst)
            note_lst = []
        header1 = ['NOTE ID', 'TITLE', 'FULL DESCRIPTION', 'TIME STAMP']
        print(tabulate(table, headers=header1,
                       tablefmt='fancy_grid', showindex='false'))

    @staticmethod
    def prompt(ask_message) -> str:
        is_valid = False
        while not is_valid:
            reply = input(ask_message)
            if (reply.isspace()) or (reply == ''):
                print('Entry cannot be empty. Try again.')
            else:
                is_valid = True
        return reply

    @staticmethod
    def print_notebook(notebook) -> None:
        for note in notebook:
            print(str(note))
