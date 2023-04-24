class Voting:
    def __init__(self, id, name, startDate, endDate, options,blockchain):
        self.id = id
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.options = options
        self.blockchain = blockchain

    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "startDate": self.startDate,
            "endDate": self.endDate,
            "options": self.options
        }
