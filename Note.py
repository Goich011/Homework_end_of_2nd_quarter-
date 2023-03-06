class Note:
    def __init__(self, name, content, date, dimens):
        self.name = name
        self.content = content
        self.date = date
        self.id = dimens

    def printNote(self):
        return "ID: {}\nНазвание: {}\n {}".format(self.id, self.name, self.content)
