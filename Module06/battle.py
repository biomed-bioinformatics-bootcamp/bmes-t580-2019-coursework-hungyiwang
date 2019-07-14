import random
import wizarad_code as wc
#from wizarad_code import Creature, Wizard, iceWizard


if __name__=='__main__':
    creature = wc.Creature('small animal', 1)
    #creature= Creature('small animal', 1)
    creatures_to_fight=[wc.Creature('small animal', 1),
                        wc.Creature('big animal',5),
                        wc.Wizard('bad wizard', 10)]
    me=wc.iceWizard('Will',8)
    me.print()

    turn_creature = random.choice(creatures_to_fight)

    #duck typing
    print('An {} emerges from the forest.'.format(turn_creature.name))
    turn_creature.print()
    if turn_creature.level < me.level:
        print('Should be easy. Its only level {}'.format(turn_creature.level))
    else:
        print('Watch out! Its level {}'.format(turn_creature.level))
    print('What do you want to do?')
    action= input('[A]ttack, [R]un, [Q]uit')
    if action.lower() =='q':
        print('See ya')
        raise SystemExit
    elif action.lower() =='a':
        while me.hp > 0 or turn_creature.hp > 0:
            if me.hp == 0 or turn_creature.hp == 0:
                break
            attack_pattern = random.choice(wc.iceWizard.attack_list)
            print(me.name+' attacks '+turn_creature.name+' by '+attack_pattern)

            if attack_pattern==wc.iceWizard.attack_list[0]:
                my_attack = me.attack_roll()
            elif attack_pattern==wc.iceWizard.attack_list[1]:
                my_attack = me.ice_ball()


            creature_lose_hp = my_attack - turn_creature.defense_roll()
            me_lose_hp = turn_creature.attack_roll() - me.defense_roll()
            if creature_lose_hp <0:
                creature_lose_hp =0
            if me_lose_hp < 0:
                me_lose_hp = 0

            print('You lose:',me_lose_hp,'hp. They lose:',creature_lose_hp,'hp.')
            me.hp = me.hp - me_lose_hp
            turn_creature.hp = turn_creature.hp - creature_lose_hp
            if me.hp < 0:
                me.hp =0
            if turn_creature.hp < 0:
                turn_creature.hp = 0
            print('Your Hp is '+ str(me.hp)+'. Their Hp are '+ str(turn_creature.hp)+'.\n')


        if turn_creature.hp == 0:
            print('you won')
            me.level_up()
        else:
            print('You lost')
    elif action.lower()=='r':
        print('You ran and hide.')