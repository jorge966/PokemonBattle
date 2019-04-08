import pokemonAttack as pokemonAtk

class Pokemon:

    attackList = [pokemonAtk.pokemonAttack("scratch", 30, 10), pokemonAtk.pokemonAttack("growl", -20, 20)]

    def __init__(self, name , hp , atk , defense, currentLevel ):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.currentLevel = currentLevel

    def getName(self):
        return self.name

    def getHP(self):
        return self.hp

    def getAttack(self):
        return self.atk

    def getDef(self):
        return self.defense

    def getAttack1(self):
        return self.attackList[0]

    def getAttack2(self):
        return self.attackList[1]

    def getAllAttacks(self):
        return self.attackList

    def getAllStats(self):
        statDict = {
            "name": self.name,
            "hp": self.hp,
            "atk": self.atk,
            "def": self.defense
        }
        return statDict
    def getAllBattle(self):
        return self.atk

    def getCurrentLevel(self):
        return self.currentLevel

    def getLevelUp(self):
        self.currentLevel = self.currentLevel + 1
        return self.currentLevel


















