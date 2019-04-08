class pokemonAttack:
    def __init__(self, attackName, attackDamage, attackPP):
        self.attackDamage = attackDamage
        self.attackPP = attackPP
        self.attackName = attackName

    def getAttackName(self):
        return self.attackName

    def getAttackDamage(self):
        return self.attackDamage

    def setAttackDamage(self, value):
        self.attackDamage = value

    def getAttackPP(self):
        return self.attackPP

    def setAttackPP(self, value):
        self.attackPP = value






