# Turn-based RPG

# Features:
# - HP
# - Attack
# - Block
# - Heal
# - Attacks are RNG-based

import time as t 
import random

class Class:
        def __init__(self, name, atk, hp, max_hp, special):
            self.name = name
            self.atk = atk
            self.hp = hp
            self.max_hp = max_hp
            self.special = special




knight_img = r"""

  ,^.
  |||
  |||       _T_
  |||   .-.[:|:].-.
  ===_ /\|  '\''  |/
   E]_|\/ \--|-|---|
   O  `'  '=[:]| A  |
          /----|  P |
         /-----`.__.'
        []"/\"--\"[]
        | \     / |
        | |     | |
      <\\\)     (///>

"""




crawl = r"""
   _________________________________________________________
 /|     -_-                                             _-  |\
/ |_-_- _                    crawl                -_- _-   -| \   
  |                      --_  -_-  _--                      | 
  |                            ,                            |
  |      .-'````````'.        '(`        .-'```````'-.      |
  |    .` |           `.      `)'      .` |           `.    |          
  |   /   |   ()        \      U      /   |    ()       \   |
  |  |    |    ;         | o   T   o |    |    ;         |  |
  |  |    |     ;        |  .  |  .  |    |    ;         |  |
  |  |    |     ;        |   . | .   |    |    ;         |  |
  |  |    |     ;        |    .|.    |    |    ;         |  |
  |  |    |____;_________|     |     |    |____;_________|  |  
  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |
  |  |  / __  ()        -|        -  |  /  __--      -   |  |
  |  | /        __-- _   |   _- _ -  | /        __--_    |  |
  |__|/__________________|___________|/__________________|__|
 /                                             _ -           \
/   -_- _ -             _- _---                       -_-  -_ \


"""

def main():
    player_name = intro(crawl)
    player_class = cls_selection(player_name)
    play_game = game(player_class)

def intro(crawl):
    
    for line in crawl.splitlines():
        print(line)
        t.sleep(0.1)

    t.sleep(0.1)
    name = input("Enter your name: ")

    t.sleep(0.1)
    
    return name

def cls_selection(name):

    Warrior = Class("Warrior", 3, 20, 20, "Blade Dance")
    Mage = Class("Mage", 7, 5, 5, "Magic Burst")
    Archer = Class("Archer", 5, 10, 10, "Triple Shot")

    for i, cls in enumerate([Warrior, Mage, Archer], start=1):

        # Display options
        print(f"{i}. {cls.name}:")
        print(f"Attack {cls.atk}")
        print(f"Health Points {cls.hp}")
        print(f"Special {cls.special}")
        print("\n")

    option = int(input(f"{name}... Choose your class: (1-3) \n"))


    # prints in if statement are for testing purposes only.
    if option == 1:
        print(vars(Warrior))
        return Warrior # returning the class object instead of the option number.
    elif option == 2:
        print(vars(Mage)) 
        return Mage # returning the class object instead of the option number.
    elif option == 3:
        print(vars(Archer))
        return Archer # returning the class object instead of the option number.
    else:
        print("Invalid option. Please choose a valid class.")
        option = cls_selection(name)

    return option

def game(play_game):

    Knight = Class("Knight", 8, 10, 10, "Slash")

    for line in knight_img.splitlines():
        print(line)
        t.sleep(0.1)

    print("You encounter a Knight.\n")

    while play_game.hp > 0 and Knight.hp > 0:

        t.sleep(0.50)

        print(f"{Knight.name} HP: {Knight.hp} ATK: {Knight.atk}")
        print("\n")

        option = int(input("1. Attack\n2. Heal\n3. Special Attack\n"))

        if option == 1:
            damage = random.randint(0, play_game.atk)

            # testing line
            print(f"{play_game.atk} how much {play_game.name} hits for by default.\n") 

            # testing line
            print(f"{damage} how much {play_game.name} hits for. Given that damage is random.\n") 

            Knight.hp -= damage # update Knight's HP

            if damage == 0:
                print(f"{play_game.name} missed!\n")
            elif damage > 0:
                print(f"{play_game.name} hit for {damage} damage.\n")
                print(f"{play_game.name} HP: {play_game.hp}\n")

        elif option == 2: 

            # fix max hp is not 20 for all classes.
            # this is a temporary fix for the heal amount.

            if play_game.hp >= play_game.max_hp:
                print(f"You cannot do this now. You are at max HP.\n")

                return game(play_game)
            elif play_game.hp < play_game.max_hp:

                heal_amount = random.randint(1, play_game.max_hp)

                # testing line
                print(f"{play_game.hp} current health prior to heal")

                # testing line
                print(f"{heal_amount} heal amount lol")

                play_game.hp += heal_amount # update player HP


                print(f"{play_game.name} has healed for {heal_amount}\n")
                print(f"{play_game.name} HP: {play_game.hp}\n")

        elif option == 3:

            print(f"this aint done yet")

            return game(play_game)
        
        print(f"{Knight.name} attacks. \n")

        damage = random.randint(0, Knight.atk)

        # testing line

        print(f"{Knight.name} has a default damage of {Knight.atk}")
        
        # testing line

        print(f"{Knight.name} hits for {damage} damage.\n")

        play_game.hp -= damage # update player HP

        if damage == 0:
            print(f"{Knight.name} missed!\n")
        elif damage > 0:
            print(f"{Knight.name} hit for {damage} damage.\n")
            print(f"{play_game.name} HP: {play_game.hp}\n")
        
        
    
    








main()