class User:
    def __init__(self, Name, Email, Folowers) -> None:
        self.Name:str = Name
        self.Email:str = Email
        self.Folowers:int = Folowers
    
    def getName(self):
        return self.Name
    
    def setName(self, Name):
        self.Name = Name

    def getEmail(self):
        return self.Email

    def setEmail(self, Email):
        self.Email = Email

    def getFolowers(self):
        return self.Folowers

    def setFolowers(self, Folowers):
        self.Folowers += Folowers