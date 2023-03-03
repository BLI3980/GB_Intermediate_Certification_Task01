
class Note:
    """Class creates a note instance"""

    def __init__(self, title, text):
        self.__id = 0
        self.title = title
        self.text = text

    @property
    def id(self):
        return self.__id

    # @property
    # def title(self):
    #     return self.title

    # @property
    # def text(self):
    #     return self.text

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    # @title.setter
    # def title(self, new_input):
    #     self.title = new_input

    # @text.setter
    # def text(self, new_input):
    #     self.text = new_input

    def __str__(self):
        return f'id: {self.id}\n'\
                f'title: {self.title}\n'\
                f'note text: {self.text}\n'

