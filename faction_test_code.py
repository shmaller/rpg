from faction import *
from careers import Archer, Wizard, Warrior, Monk
from mechanics import load_game_or_new_game

def main():
    Archers = Faction('Archers')
    Wizards = Faction('Wizards')
    Warriors = Faction('Warriors')
    Monks = Faction('Monks')

    archers_opinions = {
        'Wizards': -0.7,
        'Warriors': 0.6,
        'Monks': 0.1
    }

    wizards_opinons = {
        'Archers': -0.5,
        'Warriors': -0.1,
        'Monks': 0.7
    }

    warriors_opinions = {
        'Archers': -0.9,
        'Wizards': -0.2,
        'Monks': 0.8
    }

    monks_opinions = {
        'Archers': -0.3,
        'Warriors': 0.2,
        'Wizards': 0.5
    }

    Archers.opinions = archers_opinions
    Wizards.opinions = wizards_opinons
    Warriors.opinions = warriors_opinions
    Monks.opinions = monks_opinions

    hero = load_game_or_new_game()
    career = input("What will be thy trade?\n\
type 'a' for Archer, 'wi' for Wizard, 'wa' for Warrior, 'm' for Monk.\n\
Choose carefully, for enmities abound: ").lower()
    
    if career not in ['a','wi','wa','m']:
        print('typo')
        return main()
    
    if career == 'a':
        hero.faction = Archers
    elif career == 'wi':
        hero.faction = Wizards
    elif career == 'wa':
        hero.faction = Warriors
    elif career == 'm':
        hero.faction = Monks
    else:
        input('idk what happened.')
        return

    allegiance = float(input("How strongly do you feel connected\
to that path? 0-1: "))
    
    hero.allegiance = allegiance

    Heiffa = Archer(hero,name='Heiffa')
    Gorgo = Wizard(hero,name='Gorgo')
    Bof = Warrior(hero,name='Bof')
    Malak = Monk(hero,name='Malak')

    hero.chat(Heiffa)
    hero.chat(Gorgo)
    hero.chat(Bof)
    hero.chat(Malak)

if __name__ == '__main__':
    main()