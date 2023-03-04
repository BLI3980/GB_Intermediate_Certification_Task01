import csv
from Notes.Model.Database import Database
from Notes.Model.Note import Note
from Notes.Config.Config import source_csv


class DbCsv(Database):
    """Class interacts with csv database"""
    def __init__(self):
        super().__init__(source_csv)

    def read_db(self):  # Read from file into list of Note instances
        notebook = []
        with open(self.database, 'r', encoding='utf-8') as notes:
            for line in notes:
                lst = line.strip().split(';')
                note = Note(lst[1], lst[2])
                note.id = lst[0]
                # print(str(note))
                notebook.append(note)
        return notebook

    def save_db(self, notebook):  # From list of Notes write to file
        with open('temp.txt', 'w', encoding='utf-8', newline='') as db_csv:
            csv_writer = csv.writer(db_csv, delimiter=';')
            for note in notebook:
                csv_writer.writerow([note.id]+[note.title]+[note.text])

# Old methods:
    # def read_db(self) -> list:  # Read from file to make list of dict
    #     fields = ['id', 'title', 'description']
    #     list_of_dictionaries = []
    #     final_list = []
    #     dictionary = {}
    #     with open(self.database, 'r', encoding='utf-8') as notes:
    #         for line in notes:
    #             record = dict(zip(fields, line.strip().split(';')))
    #             list_of_dictionaries.append(record)
    #
    #     # Converting id from string type to integer type
    #     for each_dictionary in list_of_dictionaries:
    #         for (key, value) in each_dictionary.items():
    #             if value.isdigit():
    #                 value = int(value)
    #                 dictionary[key] = value
    #             else:
    #                 dictionary[key] = value
    #         final_list.append(dictionary)
    #         dictionary = {}
    #     return final_list


    # def save_db(self, updates: list) -> None:  # From list write to file
    #     with open(self.database, 'w', encoding='utf-8', newline='') as db_csv:
    #         csv_writer = csv.writer(db_csv)
    #         for row in updates:  # each dict in the list of dict
    #             csv_writer.writerow(row.values())

