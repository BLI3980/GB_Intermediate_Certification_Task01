from Notes.Model.DbCsv import DbCsv
from Notes.Model.DbJson import DbJson


class DbManager:
    """Class for selecting database format to load"""
    def load_csv_db(self):
        return DbCsv()

    def load_json_db(self):
        return DbJson()



