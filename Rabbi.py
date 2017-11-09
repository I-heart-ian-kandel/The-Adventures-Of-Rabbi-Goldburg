
"""
Sean Shmuleivch

Text based adventure game

This game is a Text based adventure game in which the
user need to navigate throught the levels of the game and defeat monsters
this is a turn based game based on stratagy, this game attempts to follow
the mechanics/dynamics of the pokemon games sort of not really but its turn based
"""
import random
import shutil
import Rabbi
columns = shutil.get_terminal_size().columns
go =(input("Before you start the game you must set the terminal size full screen :)\n Press Enter to continue\n"))
print("""
 ____  _  _  ____     __   ____  _  _  ____  __ _  ____  _  _  ____  ____  ____     __  ____ 
(_  _)/ )( \(  __)   / _\ (    \/ )( \(  __)(  ( \(_  _)/ )( \(  _ \(  __)/ ___)   /  \(  __)
  )(  ) __ ( ) _)   /    \ ) D (\ \/ / ) _) /    /  )(  ) \/ ( )   / ) _) \___ \  (  O )) _) 
 (__) \_)(_/(____)  \_/\_/(____/ \__/ (____)\_)__) (__) \____/(__\_)(____)(____/   \__/(__)
 

 ____    ____  ____   ____   ____       ____   ___   _      ___    ____   __ __  ____    ____ 
|    \  /    ||    \ |    \ |    |     /    | /   \ | |    |   \  |    \ |  |  ||    \  /    |
|  D  )|  o  ||  o  )|  o  ) |  |     |   __||     || |    |    \ |  o  )|  |  ||  D  )|   __|
|    / |     ||     ||     | |  |     |  |  ||  O  || |___ |  D  ||     ||  |  ||    / |  |  |
|    \ |  _  ||  O  ||  O  | |  |     |  |_ ||     ||     ||     ||  O  ||  :  ||    \ |  |_ |
|  .  \|  |  ||     ||     | |  |     |     ||     ||     ||     ||     ||     ||  .  \|     |
|__|\_||__|__||_____||_____||____|    |___,_| \___/ |_____||_____||_____| \__,_||__|\_||___,_|                                                                                              
""".center(columns))



#rules for game
go = input("""The instructions for this game are as follows the
objective of the game is to level up by defeating servents of the
all powerful zanis you attack the srevents in a sudo random turn based format 
moves include dodge, attack , and attack with a chance to dodge
once healh is below zero the player will respawn with one less life each player
only two lives per game.
you will level up from defeting servents
 press Enter to continue\n""".center(columns))
#player choice
go =  input("its time to pick a player you have three choices; however, all of the choises will be Rabbi Goldburg \njust him from a different dimensions\npress Enter to continue \n ".center(columns))
#choice 1
fast_rabbi = input("""Rabbi Goldburg number one grew up in the country, and practices reform judaism he
was a track star at his jewish private school he is fast but weaker then the other players
this translates to more effective doging but less effective attacks also he is more effective
against fire and less effective against water\n press Enter to continue\n""".center(columns))
#choice 2
strong_rabbi = input("""Rabbi Goldburg number two grew up in the suburbs, and practices conservitive judaism
when he isn't practicing judaism, or praying he's playing lacrosse with the other Rabbi's
he was on the varsity lacrosse team at Pennsbury High School he is strong but slower then the other players
this translates to less effective doging but more effective attacks also he is more effective
against faku and less effective against fire type servents\n press Enter to continue\n""")
#choice 3
smart_rabbi = input ("""
Rabbi Goldburg number three grew up in the city, and practices orthodox judaism
his intelligence, and wisdom is unfathomable, he has dedicated his entire life to worshipping G-d
he is not as strong ar fast as the others but his wit overcomes all. Rabbi Goldburg number three
was the all state chess champion at his catholic school where he overcame all obstacles of being the only Jew at his school 
his wit translates to medium effective doging and medium effective attacks but, more health also he is more effective
against water and less effective against faku type servents\n press Enter to continue\n""")

# variables global important
global hp
global speed
global power
global level

# base values
level = 0.0
hp = 0.0
speed = 0.0
attack = 0.0


choice = (" ")
# doesn't end until right input
while ((choice != ("player 1")) and (choice != ("player 2")) and (choice != ("player 3"))):
    choice = input('now make your choice enter: "player 1", "player 2" or "player 3": ').lower()
    if ((choice != ("player 1")) and (choice != ("player 2")) and (choice != ("player 3"))):
        print("please input \"player 1\", \"player 2\", or \"player 3\".")
    
# converts to more specific for use with stings
def quality(choice):
    if choice == "player 1":
        return ("Fast Rabbi")
    elif choice == "player 2":
        return ("Strong Rabbi")
    else:
        return ("Smart Rabbi")
#string     
go = input(("\nYou have chosen "+choice+" the "+quality(choice)+" have fun!\n Press enter to continue\n").center(columns))

# starting stats per choice
if choice == ("player 1"):
    hp = 50.0
    speed = 10.0
    attack = 7.5
elif choice == ("player 2"):
    hp = 50.0
    speed = 7.5
    attack = 10.0
elif choice == ("player 3"):
    hp = 65.0
    speed = 7.5
    attack = 7.5

# story
go = input(quality(choice)+""", Rabbi Goldburg recives a phone call from the president of the
united states and former Pennsbury High School principal, Mr.fry, he is calling from a
top secret bunker the government needs Rabbi Goldburg's help. The
Zanis has attacked New York City the Pentagon and the white house\n Press enter to continue\n""")


location = (""" """)

# doesn't end until correct input
while ((location != ("A")) and (location != ("B")) and (location != ("C"))):
    location = input("""\nWhere will you go to find the Zanis
    A. Pentagon
    B. White House
    C. New York City
    input "A" "B" or "C": """).upper()
    if ((location != ("A")) and (location != ("B")) and (location != ("C"))):
        print("\nplease input \"A\", \"B\", or \"C\".")

# converts input to more specific
if location == "A":
    location = " The Pentagon"
    print ("You have chosen the Pentagon")
elif location == "B":
    location = "The White House"
    print ("You have chosen the White House")
else:
    location = "New York City"
    print("You have chosen the New York City")

# story
go = input("\nAfter days of travel and prep you have arrived at "+ location+" ready to fight and defent you country and beliefs\n Press enter to continue\n")
go = input("\nas you look upon a desolate "+location+" you think about the dark times and and how you Rabbi Goldburg are the savior\n press enter to continue\n")
go = input ("\nyou put all thoughts aside because you know now is time, time to fight you go and find your first servent to fight\n press enter to continue\n")

# for loop 1 2 3 go, just for effect, story
for loop in ("123\nGO"):
  print (loop)
  # continue to battle
go =  input("\n Press enter to continue\n".center(columns))

#sets val's to base
monster_power = 0.0
monster_health = 0.0
monster_speed = 0.0

#functions for monster stats based on level
def fire(level):
        global monster_power
        global monster_health
        global monster_speed
        monster_power = 0.0
        monster_health = 0.0
        monster_speed = 0.0
        if level == 0:
            monster_power =+ 5.0
            monster_health =+ 31.0
            monster_speed =+ 4.0
        elif level == 1:
            monster_power =+ 15.0
            monster_health =+ 100.0
            monster_speed =+ 11.5 
        elif level == 2:
            monster_power =+40.0
            monster_health =+ 200.0
            monster_speed =+ 30.0
def water(level):
        global monster_power
        global monster_health
        global monster_speed
        monster_power = 0.0
        monster_health = 0.0
        monster_speed = 0.0
        if level == 0:
            monster_power =+ 4.0
            monster_health =+ 30.0
            monster_speed =+ 5.0
        elif level == 1:
            monster_power =+ 11.5
            monster_health =+ 10.0
            monster_speed =+ 15.0
        elif level == 2:
            monster_power =+ 30.0
            monster_health =+ 200.0
            monster_speed =+ 40.0
def faku(level):
        global monster_power
        global monster_health
        global monster_speed
        monster_power = 0.0
        monster_health = 0.0
        monster_speed = 0.0
        if level == 0:
            monster_power =+ 4.0
            monster_health =+ 35.0
            monster_speed =+ 4.0
        elif level == 1:
            monster_power =+ 11.5
            monster_health =+ 97.5
            monster_speed =+ 11.5
        elif level == 2:
            monster_power =+ 30.0
            monster_health =+ 260.0
            monster_speed =+ 30.0

random_mob = [fire, water, faku]

#function to be implemented in the future
"""
def hp_cap(hp, level, attribute):
  if level == 0:
    if (choice == ("player 1 " or "player 2")) and hp > 50 :
      hp = 50
    elif (choice == "player 3") and hp > 65:
      hp = 65
  elif level == 1:
    if (choice == ("player 1 " or "player 2")) and hp > 100 :
      hp = 100
    elif attribute == "faku type" and hp > 130:
      hp = 130
  elif level == 2:
    if (choice == ("player 1 " or "player 2")) and hp > 200 :
      hp = 200
    elif (choice == "player 3") and hp > 260:
      hp = 260
"""

def fight():# main super important function
    random.choice(random_mob)(level)# pick monster
    # globals relevent for function
    global monster_speed
    global monster_health
    global monster_power
    global hp
    global speed
    global attack
    attribute = ("")
    # which type of monster
    # every level up the servents are 25% stronger level 2 they are 100% of player stats level 0, 50%, level one 75&
    if ((monster_health == 31.0) and (monster_health == 100.0) and (monster_health == 200.0)):
      attribute = ("Fire type")
    elif ((monster_health == 30.0) and (monster_health == 101.0) and (monster_health == 200.0)):
      attribute = ("Water type")
    elif ((monster_health == 35.0) and (monster_health == 97.50) and (monster_health == 260.0)):
      attribute = ("faku type")
    # effects player stats based on player type strengths and weaknesses 
    if (attribute == "Fire type") and choice == "player 1":
        speed *= 1.25
        hp *= 1.25
        attack *= 1.25
    elif (attribute == "Fire type") and choice == "player 2":
        speed *= .75
        hp *= .75
        attack *= .75
    elif (attribute == "Water type") and choice == "player 1":
        speed *= .75
        hp *= .75
        attack *= .75
    elif (attribute == "Water type") and choice == "player 3":
        speed *= 1.25
        hp *= 1.25
        attack *= 1.25
    elif (attribute == "faku type") and choice == "player 2":
        speed *= 1.25
        hp *= 1.25
        attack *= 1.25
    elif (attribute == "faku type") and choice == "player 3":
        speed *= .75
        hp *= .75
        attack *= .75
    #info for user
    go = input("""you have stumbled upon a """+ (attribute)+""" type servent with """+str(monster_power)+""" power, """+ str(monster_health)+""" health, and """+ str(monster_speed)+""" speed get ready to fight\n press enter to continue\n""")
    # while loop continues until break
    while True:
        # the user will always be faster unless level is 2 but i didnt get that far in the game oops
        if speed >= monster_speed:
            # 60% chance of moving first if player is faster
            move_first_faster =  random.randint(1,5)
            if ((move_first_faster == (1)) or (move_first_faster == (2)) or (move_first_faster == (3))):
                print ("you move because you are faster pick your move")
                move = (""" """)
                # doesn't stop until correct input
                while ((move != ("A")) and (move != ("B")) and (move != ("C"))):
                    move = input("""
                        Pick your move
                            A. Attack
                            B. Dodge and gain 5 health back
                            C. Attack with a chance to dodge also
                            please input \"A\", \"B\", or \"C\".: """).upper()
                    if ((move != ("A")) and (move != ("B")) and (move != ("C"))):
                        print(("\nplease input \"A\", \"B\", or \"C\".\n"))
                # if move is a
                if move == ("A"):
                    # 80% chance of sucessfully attacking
                    move_probability_a = random.randint(1,5)
                    if ((move_probability_a == (1)) or (move_probability_a == (2)) or (move_probability_a == (3)) or (move_probability_a == (4))):
                        #subtracts user attack from monster health and stores it in monster_health
                        monster_health = monster_health - attack
                        # user info
                        go = (input("you attack! you do "+ str(attack)+" damge to the servent the servent now has "+ str(monster_health)+" hp\n press enter to continue\n"))
                    else:
                        # if the move misses
                        hp = hp - monster_power # player health minus the monster attack value then stores in hp
                        # player info
                        go = input("you miss! the monster does "+ str(monster_power)+" damage you now have "+ str(hp)+" health\n press enter to continue\n")
                elif move == ("B"):
                    move_probability_b = random.randint(1,5)# 80% to sucessfully dodge
                    if ((move_probability_b == (1)) or (move_probability_b == (2)) or (move_probability_b == (3)) or (move_probability_b == (4))):
                        hp = hp + 5
                        print ("doge is sussful and you gain 5 health you now have"+ str(hp)+" health\n")
                    else:# 20% to miss and take monster damage
                        hp = hp - monster_power
                        print ("dodge is unsucessful monster attacks and you lose "+str(monster_power)+" health you now have "+ str(hp)+" health\n")
                else:
                    move_probability_c = random.randint(1,5)# 20% dodge and attack 20% miss 60% attack
                    if (move_probability_c == (1)):# if attack and dodge
                        hp = hp + 5 # stores value of hp
                        monster_health = monster_health - attack
                        print ("you attack! you do "+ str(attack)+" damge to the servent the servent now has "+ str(monster_health)+" hp also you dodge and gain 5 health you now have "+ str(hp)+" health\n")
                    elif ((move_probability_c == (2)) or (move_probability_c == (3)) or (move_probability_c == (4))):
                        monster_health = monster_health - attack # servent takes damage stores in monster_health
                        print ("you attack you do "+ str(attack)+" damage the servent now has "+ str(monster_health)+" health\n")
                    else:# if miss
                        hp = hp - monster_power
                        # player info
                        go = input("you miss! the monster does "+ str(monster_power)+" damage you now have "+ str(hp)+" health\n press enter to continue\n")
            else:# if they dont go despite speed. (40% chance)
                print("The servent attacks even though you are faster\n")
                # the servent  attacks
                servent_attack = random.randint(1,5)
                if servent_attack == 1:# servrnt misses 20% chance
                    hp = hp + 5
                    go = input("the servent misses! and you gain 5 health you now have "+ str(hp)+" health\n press enter to continue\n")
                else:
                    hp = hp - monster_power
                    go = input("the servent attacks! and you lose "+ str(monster_power)+" health you now have "+ str(hp) +" left\n press enter to continue\n")
        elif speed < monster_speed:# if slower then monster
            # 33% chance of moving first if player is slower
            move_first_slower = random.randint(1,3)
            if move_first_slower == (1):
                print ("you move despite the fact you are slower. pick your move")
                move = (""" """)
                # doesn't stop until correct input
                while ((move != ("A")) and (move != ("B")) and (move != ("C"))):
                    move = input("""
                        Pick your move
                            A. Attack
                            B. Dodge and gain 5 health back
                            C. Attack with a chance to dodge also
                            please input \"A\", \"B\", or \"C\".: """).upper()
                    if ((move != ("A")) and (move != ("B")) and (move != ("C"))):
                        print(("\nplease input \"A\", \"B\", or \"C\".\n"))
                # if move is a
                if move == ("A"):
                    # 80% chance of sucessfully attacking
                    move_probability_a = random.randint(1,5)
                    if ((move_probability_a == (1)) or (move_probability_a == (2)) or (move_probability_a == (3)) or (move_probability_a == (4))):
                        #subtracts user attack from monster health and stores it in monster_health
                        monster_health = monster_health - attack
                        # user info
                        go = (input("you attack! you do "+ str(attack)+" damge to the servent the servent now has "+ str(monster_health)+" hp\n press enter to continue\n"))
                    else:
                        # if the move misses
                        hp = hp - monster_power # player health minus the monster attack value then stores in hp
                        # player info
                        go = input("you miss! the monster does "+ str(monster_power)+" damage you now have "+ str(hp)+" health\n press enter to continue\n")
                elif move == ("B"):
                    move_probability_b = random.randint(1,5)# 80% to sucessfully dodge
                    if ((move_probability_b == (1)) or (move_probability_b == (2)) or (move_probability_b == (3)) or (move_probability_b == (4))):
                        hp = hp + 5
                        print ("doge is sussful and you gain 5 health you now have"+ str(hp)+" health\n")
                    else:# 20% to miss and take monster damage
                        hp = hp - monster_power
                        print ("dodge is unsucessful monster attacks and you lose "+str(monster_power)+" health you now have "+ str(hp)+" health\n")
                else:
                    move_probability_c = random.randint(1,5)# 20% dodge and attack 20% miss 60% attack
                    if (move_probability_c == (1)):# if attack and dodge
                        hp = hp + 5 # stores value of hp
                        monster_health = monster_health - attack
                        print ("you attack! you do "+ str(attack)+" damge to the servent the servent now has "+ str(monster_health)+" hp also you dodge and gain 5 health you now have "+ str(hp)+" health\n")
                    elif ((move_probability_c == (2)) or (move_probability_c == (3)) or (move_probability_c == (4))):
                        monster_health = monster_health - attack # servent takes damage stores in monster_health
                        print ("you attack you do "+ str(attack)+" damage the servent now has "+ str(monster_health)+" health\n")
                    else:# if miss
                        hp = hp - monster_power
                        # player info
                        go = input("you miss! the monster does "+ str(monster_power)+" damage you now have "+ str(hp)+" health\n press enter to continue\n")
            elif (move_first_slower == (2)) or (move_first_slower == (3)):# if they dont go despite speed. (66% chance)
                print("The servent attacks because you are slower\n")
                # the servent  attacks
                servent_attack = random.randint(1,5)
                if servent_attack == 1:# servrnt misses 20% chance
                    hp = hp + 5
                    go = input("the servent misses! and you gain 5 health you now have "+ str(hp)+" health\n press enter to continue\n")
                else:
                    hp = hp - monster_power
                    go = input("the servent attacks! and you lose "+ str(monster_power)+" health you now have "+ str(hp) +" left\n press enter to continue\n")
        if (hp <= 0):# if player dies 
            global player_lives
            player_lives = 2
            player_lives = player_lives - 1
            print ("oops you have died minus one lives you now have "+ str(player_lives)+" continue with one less life")
            if player_lives <= 0:# game over if lives is less then or equal to zero
                print("""
  /$$$$$$                                           /$$$$$$                               
 /$$__  $$                                         /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$  \ $$ /$$    /$$ /$$$$$$   /$$$$$$ 
| $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$      | $$  | $$|  $$  /$$//$$__  $$ /$$__  $$
| $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$      | $$  | $$ \  $$/$$/| $$$$$$$$| $$  \__/
| $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/      | $$  | $$  \  $$$/ | $$_____/| $$      
|  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$      |  $$$$$$/   \  $/  |  $$$$$$$| $$      
 \______/  \_______/|__/ |__/ |__/ \_______/       \______/     \_/    \_______/|__/""")
                while True: # waits for right input   
                    again = input("would you like to play again?\n input yes or no\n").lower()
                    if again == "yes":
                        break
                        Rabbi# runs the entrie program again if yes
                    elif again == "no":
                        break
                        go = input("thanks for playing\n press enter to exit\n")# doesn't exit oops
                    else:
                        print ("please input \"yes\" or \"no\".")# if incorrect asks for correct
            break#breaks outtermost loop
        elif monster_health <= 0:# defeted
            #user information
            print ("good job you have defeted the servent or even defeted into the negitives! and gained 10 exp")
            break

fight()#once the function is used twice (level + 1), four times level + 2 #battle 1
if choice == ("player 1"): # sets stats back after battle
    hp = 50.0
    speed = 10.0
    attack = 7.5
elif choice == ("player 2"):
    hp = 50.0
    speed = 7.5
    attack = 10.0
elif choice == ("player 3"):
    hp = 65.0
    speed = 7.5
    attack = 7.5

#story branching
go = (input (("Great job with that battle all of your stats have been reset but that \nservent is only a peice of the puzzle you have a long journey ahead of you\n press enter to continue\n")))

if location == "The Pentagon":
    go = input("""You step into the pentagon after your battle near the entrance
you know there is much hardship ahead but you know what you need to do you continue on your quest to find zanis\n press enter to continue\n """)
elif location == "The White House":
    go = input("""You step into the White house after your battle near the entrance
you know there is much hardship ahead but you know what you need to do you continue on your quest to find zanis\n press enter to continue\n """)
elif location == "New York City":
    go = input("""You continue on the streets after your battle on 5th ave
you know there is much hardship ahead but you know what you need to do you continue on your quest to find zanis\n press enter to continue\n """)

#fun trick
go = input("you are approached by another servent get ready to fight\n press enter to continue\n")
for loop in ("123\nGO"):
  print (loop)
go =  input("\n Press enter to continue\n".center(columns))
                
fight()#battle 2
level += 1# after battle level up, every two battles level up
if choice == ("player 1"): # sets stats back after battle plus level_up stats times two
    hp = 100.0
    speed = 20.0
    attack = 15.0
elif choice == ("player 2"):
    hp = 100.0
    speed = 15.0
    attack = 20.0
elif choice == ("player 3"):
    hp = 130.0
    speed = 15.0
    attack = 15.0
#user info
go = input("you leveled up and all your stats doubled get ready for tougher monsters\n press enter to continue\n")
go = input("""good job with that battle but it looks like there is nothing here the president calls and tells you to fly to a
different location or the same location to try to find the zanis you can check one more location to try to find zanis before he takes over\n press enter to continue\n""")


while ((location != ("A")) and (location != ("B")) and (location != ("C"))):#waits for right input to break
    location = input("""\nWhere will you go to find the Zanis
    A. Pentagon
    B. White House
    C. New York City
    input "A" "B" or "C": """).upper()
    if ((location != ("A")) and (location != ("B")) and (location != ("C"))):
        print("\nplease input \"A\", \"B\", or \"C\".")
# branching
if location == "A":
    location = " The Pentagon"
    print ("You have chosen the Pentagon")
elif location == "B":
    location = "The White House"
    print ("You have chosen the White House")
else:
    location = "New York City"
    print("You have chosen the New York City")

# story
go = input("\nAfter days of travel and prep you have arrived at "+ location+" ready to fight and defent you country and beliefs\n Press enter to continue\n")
go = input("\nas you look upon a desolate "+location+" you think about the dark times and and how you Rabbi Goldburg are the savior\n press enter to continue\n")
go = input ("\nyou put all thoughts aside because you know now is time, time to fight you go and find your servent to fight\n press enter to continue\n")

#fun
for loop in ("123\nGO"):
  print (loop)
go =  input("\n Press enter to continue\n".center(columns))
fight()# battle 3

if choice == ("player 1"): # sets stats back after battle
    hp = 100.0
    speed = 20.0
    attack = 15.0
elif choice == ("player 2"):
    hp = 100.0
    speed = 15.0
    attack = 20.0
elif choice == ("player 3"):
    hp = 130.0
    speed = 15.0
    attack = 15.0
go = input("good job, time for your last battle but where is zanis?\n press enter to continue\n")
#fun
for loop in ("123\nGO"):
  print (loop)
go =  input("\n Press enter to continue\n".center(columns))

fight()
level += 1
if choice == ("player 1"): # sets stats back after battle #game not done temporarily ended
    hp = 200.0
    speed = 40.0
    attack = 30.0
elif choice == ("player 2"):
    hp = 200.0
    speed = 30.0
    attack = 40.0
elif choice == ("player 3"):
    hp = 260.0
    speed = 30.0
    attack = 30.0
#game not done temporarily ended because of time constraints 
#story
go = input("you have compleated your quest but you havent found zanis???\n you start to call the president to inform him \n press enter to continue\n")
go = input("""but wait you think to yourself maybe there was never a zanis
maybe zanis just represented all the societal problems of today maybe zanis
was just an idea of negitivity and those servents were just little bits of negitivity and you rabbi goldburg
are in fact the savior with your faith, wisdom, power, and speed you can eliminate negitivity in this world
\n press enter to continue\n""")

ending = """"""
while True:# different endings waits for right input
    ending = input("""
what will you do next
A. call the president
B. quit being a rabbi
C. walk off into the mist in search of zanis
D. run for president
E. write a text based adventure game
F. invent the iphone
""").upper()
    if (ending != "A") and (ending != "B") and (ending != "C") and (ending != "D") and (ending != "E") and (ending != "F"):
        print ("please enter a letter A-F")
    else:
        break
# a throught f are very similar   
if ending == "A":
    go = input("The president is zanis and destroy's the world oops you were wrong")
    print("""
  /$$$$$$                                           /$$$$$$                               
 /$$__  $$                                         /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$  \ $$ /$$    /$$ /$$$$$$   /$$$$$$ 
| $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$      | $$  | $$|  $$  /$$//$$__  $$ /$$__  $$
| $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$      | $$  | $$ \  $$/$$/| $$$$$$$$| $$  \__/
| $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/      | $$  | $$  \  $$$/ | $$_____/| $$      
|  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$      |  $$$$$$/   \  $/  |  $$$$$$$| $$      
 \______/  \_______/|__/ |__/ |__/ \_______/       \______/     \_/    \_______/|__/""")
    while True:    
        again = input("would you like to play again?\n input yes or no\n press enter to continue\n").lower()
        if again == "yes":
            break
            Rabbi
        elif again == "no":
            break
            go = input("thanks for playing\n press enter to exit\n")
        else:
            print ("please input \"yes\" or \"no\".")
elif ending == "B":
    go = input("you have quit being a rabbi and lost your faith darkness takes over the world\n press enter to continue\n")
    print("""
  /$$$$$$                                           /$$$$$$                               
 /$$__  $$                                         /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$  \ $$ /$$    /$$ /$$$$$$   /$$$$$$ 
| $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$      | $$  | $$|  $$  /$$//$$__  $$ /$$__  $$
| $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$      | $$  | $$ \  $$/$$/| $$$$$$$$| $$  \__/
| $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/      | $$  | $$  \  $$$/ | $$_____/| $$      
|  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$      |  $$$$$$/   \  $/  |  $$$$$$$| $$      
 \______/  \_______/|__/ |__/ |__/ \_______/       \______/     \_/    \_______/|__/""")
    while True:    
        again = input("would you like to play again?\n input yes or no\n press enter to continue\n").lower()
        if again == "yes":
            break
            Rabbi
        elif again == "no":
            break
            go = input("thanks for playing\n press enter to exit\n")
        else:
            print ("please input \"yes\" or \"no\".")
elif ending == "C":
    go = input("you walk off and are consumed by the darkness oops\n press enter to continue\n")
    print("""
  /$$$$$$                                           /$$$$$$                               
 /$$__  $$                                         /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$  \ $$ /$$    /$$ /$$$$$$   /$$$$$$ 
| $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$      | $$  | $$|  $$  /$$//$$__  $$ /$$__  $$
| $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$      | $$  | $$ \  $$/$$/| $$$$$$$$| $$  \__/
| $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/      | $$  | $$  \  $$$/ | $$_____/| $$      
|  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$      |  $$$$$$/   \  $/  |  $$$$$$$| $$      
 \______/  \_______/|__/ |__/ |__/ \_______/       \______/     \_/    \_______/|__/""")
    while True:    
        again = input("would you like to play again?\n input yes or no\n press enter to continue\n").lower()
        if again == "yes":
            break
            Rabbi
        elif again == "no":
            break
            go = input("thanks for playing\n press enter to exit\n")
        else:
            print ("please input \"yes\" or \"no\".")
elif ending == "D":
    go = input("you run for POTUS and win! then you eliminate all darkness\n press enter to continue\n")
    print("""
 _  _  _____  __  __    _    _  ____  _  _ 
( \/ )(  _  )(  )(  )  ( \/\/ )(_  _)( \( )
 \  /  )(_)(  )(__)(    )    (  _)(_  )  ( 
 (__) (_____)(______)  (__/\__)(____)(_)\_)
""")
    while True:    
        again = input("would you like to play again?\n input yes or no\n press enter to continue\n").lower()
        if again == "yes":
            break
            Rabbi
        elif again == "no":
            break
            go = input("thanks for playing\n press enter to exit\n")
        else:
            print ("please input \"yes\" or \"no\".")
elif ending == "E":
    go = input("your game is super awesome and Mrs.purdy gives you 100% even though it was late\n press enter to continue\n")
    print("""
 _  _  _____  __  __    _    _  ____  _  _ 
( \/ )(  _  )(  )(  )  ( \/\/ )(_  _)( \( )
 \  /  )(_)(  )(__)(    )    (  _)(_  )  ( 
 (__) (_____)(______)  (__/\__)(____)(_)\_)
""")
    while True:    
        again = input("would you like to play again?\n input yes or no\n press enter to continue\n").lower()
        if again == "yes":
            break
            Rabbi
        elif again == "no":
            break
            go = input("thanks for playing\n press enter to exit\n")
        else:
            print ("please input \"yes\" or \"no\".")
else:
    go = input("you invent the iphone and make a lot of money then give it all to charity and darkness is eliminated\n press enter to continue\n")
    print("""
 _  _  _____  __  __    _    _  ____  _  _ 
( \/ )(  _  )(  )(  )  ( \/\/ )(_  _)( \( )
 \  /  )(_)(  )(__)(    )    (  _)(_  )  ( 
 (__) (_____)(______)  (__/\__)(____)(_)\_)
""")
    while True:    
        again = input("would you like to play again?\n input yes or no\n press enter to continue\n").lower()
        if again == "yes":
            break
            Rabbi
        elif again == "no":
            break
            go = input("thanks for playing\n press enter to exit\n")
        else:
            print ("please input \"yes\" or \"no\".")
