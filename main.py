class Game:
    def __init__(self, name, age, genre, rating):
        self.name = name
        self.age = age
        self.genre = genre
        self.rating = rating


    def getinfo(self):
        return(self.name + " : " + self.genre)
    def updategenre(self, newgenre):
        self.genre = newgenre

Var1 = Game("Mortal Kombat", "20", "Fighting", "21")
var2 = Game("Mario", 20, "Fantasy", 8)

print(Var1.getinfo())
Var1.updategenre("racing")
print(Var1.getinfo())
