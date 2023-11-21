from faction import *
from careers import Archer, Wizard, Warrior, Monk
from mechanics import load_game_or_new_game

def main():
    Archers = Faction('Archers')
    Wizards = Faction('Wizards')
    Warriors = Faction('Warriors')
    Monks = Faction('Monks')

    archers_opinions = {
        Archers: 0.6,
        Wizards: -0.7,
        Warriors: 0.6,
        Monks: 0.1
    }

    wizards_opinons = {
        Wizards: 0.3,
        Archers: -0.5,
        Warriors: -0.1,
        Monks: 0.7
    }

    warriors_opinions = {
        Warriors: 0.9,
        Archers: -0.9,
        Wizards: -0.2,
        Monks: 0.8
    }

    monks_opinions = {
        Monks: 0.8,
        Archers: -0.3,
        Warriors: 0.2,
        Wizards: 0.5
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

    allegiance = float(input("How strongly do you feel connected \
to that path? 0-1: "))
    
    hero.allegiance = allegiance

    Heiffa = Archer(name='Heiffa')
    Gorgo = Wizard(name='Gorgo')
    Bof = Warrior(name='Bof')
    Malak = Monk(name='Malak')

    Heiffa.faction = Archers
    Gorgo.faction = Wizards
    Bof.faction = Warriors
    Malak.faction = Monks

    Heiffa.allegiance = 1
    Heiffa.CHM = 1

    Gorgo.allegiance = 0.2
    Gorgo.CHM = 20

    Bof.allegiance = 1
    Bof.CHM = 8

    Malak.allegiance = 0.7
    Malak.CHM = 100

    hero.CHM = 100

    print(f'''
          Hero CHM: {hero.CHM}
          Hero faction: {hero.faction.name}
          
          Heiffa CHM: {Heiffa.CHM}
          Heiffa opinion: {Heiffa.determine_response(hero)}
          Heiffa factional: {Heiffa.get_factional_opinion(hero)}
          Archers factional: {Archers.opinion(hero)}

          Gorgo CHM: {Gorgo.CHM}
          Gorgo opinion: {Gorgo.determine_response(hero)}
          Gorgo factional: {Gorgo.get_factional_opinion(hero)}
          Wizards factional: {Wizards.opinion(hero)}

          Bof CHM: {Bof.CHM}
          Bof opinion: {Bof.determine_response(hero)}
          Bof factional: {Bof.get_factional_opinion(hero)}
          Warriors factional: {Warriors.opinion(hero)}
          
          Malak CHM: {Malak.CHM}
          Malak opinion: {Malak.determine_response(hero)}
          Malak factional: {Malak.get_factional_opinion(hero)}
          Monks factional: {Monks.opinion(hero)}
          ''')

    Heiffa.chat(hero)
    Gorgo.chat(hero)
    Bof.chat(hero)
    Malak.chat(hero)

if __name__ == '__main__':
    main()