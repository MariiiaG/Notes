class Note :
    def __init__(self, title, body, id = None, date = None) :
        self.id = id
        self.title = title
        self.body = body
        self.date = date
    def __str__(self) -> str:
        return "Note id: " + self.id + "\nTitle : " + self.title + "\nBody : " + self.body + "\Date : " + self.date