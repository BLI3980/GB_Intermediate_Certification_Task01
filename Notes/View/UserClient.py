from tabulate import tabulate
from emoji import emojize


class UserClient:
    """Class gets information from user"""
    def __init__(self):
        self.is_ok = None

    @staticmethod
    def greeting():
        return print('\nWelcome to notebook app!')

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
            except TypeError:
                print('This is not a number. Try again. ')
        return select  # Choice number

    def show_menu(self) -> int:
        print("\n" + "=" * 35)
        print(emojize(":play_button:  Choose an action from the list below: "))
        print(emojize("1. :department_store: Show the entire notebook"))
        print(emojize("2. :NEW_button: Create new note"))
        print(emojize("3. :magnifying_glass_tilted_left: Find a note by ID"))
        print(emojize("4. :magnifying_glass_tilted_right: Find a note by Title"))
        print(emojize("5. :memo: Edit a note"))
        print(emojize("6. :cross_mark: Delete a note"))
        print(emojize("8. :floppy_disk: Export notebook into csv file"))
        print(emojize("9. :dvd: Export notebook into json file"))
        print(emojize("10.:stop_button:End the work"))
        print("=" * 35 + "\n")
        self.is_ok = False
        while not self.is_ok:
            try:
                select = int(input("Enter a number of corresponding action: "))
                self.is_ok = True
                if select not in range(1, 11):
                    self.is_ok = False
                    print('Incorrect number. Try again.')
            except ValueError:
                print('This is not a number. Try again.')
        return select

    def get_new_note_info(self) -> tuple:
        title = self.prompt('Enter the title for the note: ')
        text = self.prompt('Enter the details of the note: ')
        return title, text

    def print_tabulated_table(self, list_of_dictionaries) -> None:
        table = []
        temp = []
        for dictionary in list_of_dictionaries:
            for value in dictionary.values():
                # Get a list of values from each dictionary.
                temp.append(value)
            # Get a list of lists.
            table.append(temp)
            temp = []
        header1 = ['NOTE ID', 'TITLE', 'FULL DESCRIPTION']
        print(tabulate(table, headers=header1,
                       tablefmt='fancy_grid', showindex='false'))

    def prompt(self, ask_message):
        return input(ask_message)



# x = UserClient()
# print(x.get_new_note_info())
