
class Note:
    """Class creates a note instance"""

    def __init__(self, title, text):
        self.__id = 0
        self.title = title
        self.text = text

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    def __str__(self):
        return f'\n{"=" * 30}\n'\
            f'id: {self.id}\n'\
            f'title: {self.title}\n'\
            f'note text: {self.text}\n' \
               f'\n{"=" * 30}'\

