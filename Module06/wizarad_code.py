import random

class Creature(object):

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp =level*2*random.randint(15,20)


    def print(self):
        print('Name:', self.name, 'Level:', self.level,'Hp:',self.hp)

    def attack_roll(self):
        die =random.randint(1,20)
        return die*self.level

    def defense_roll(self):
        die = random.randint(1,20)
        return die*self.level

class Wizard(Creature):

    def __init__(self, name, level, typ=None):

        self.name=name
        self.level=level
        self.hp =level*2*random.randint(15,20)
        self.typ=typ


    def print(self):
        print('Name:', self.name, 'Level:', self.level, 'Hp:',self.hp,'Type:', self.typ)

    def level_up(self):
        self.level += 1

    def level_down(self):
        self.level -= 1


class iceWizard(Wizard):

    def __init__(self, name, level, typ='ice'):
        self.name = name
        self.level = level
        self.hp = level * 2 * random.randint(15, 20)
        self.typ = typ

    def ice_ball(self):
        die = random.randint(1, 20)
        return die * 1.2*self.level
    attack_list=['staff','ice ball']

if __name__== '__main__':

    first_creature = Creature('small animal', 1)
    second_creature = Creature('big animal', 10)
    first_wizard=Wizard('Will',10, typ='fire')
    second_wizard= iceWizard('Joe',5)

    #print(first_creature.name, first_creature.level)
    first_creature.print()
    #print(second_creature.name, second_creature.level)
    second_creature.print()
    first_wizard.print()
    second_wizard.print()

    first_wizard.level_up()
    first_wizard.level_up()
    first_wizard.level_up()

    first_wizard.print()

    print(first_creature.attack_roll(), second_creature.defense_roll())