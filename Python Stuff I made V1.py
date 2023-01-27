# ===== Imports stuff down here ======
import random
import time
import os
# ====================================

def calcu():
  while True:
    print("===== Sam's Python Calculator =====")
    print(" 1 : Addition ")
    print(" 2 : subtraction")
    print(" 3 : division")
    print(" 4 : squared")
    print(" 5 : Multiply")
    selection = int(input("Please select a funciton : "))
    if selection == 1:
      firstNumberAddition = float(input("FIRST NUMBER : "))
      secondNumberAddition = float(input("SECOND NUMBER : "))
      answer = firstNumberAddition + secondNumberAddition
      print("answer :",answer)
      print("")
      print("Please Enter N to Try anothere problem or Enter Y to to exit")
    elif selection == 2:
      firstNumberSub = float(input("FIRST NUMBER : "))
      secondNumberSub = float(input("SECOND NUMBER : "))
      answer = firstNumberSub - secondNumberSub
      print("answer :",answer)
      print("")
      print("Please Enter N to Try anothere problem or Enter Y to exit")
    elif selection == 3:
      firstNumberDiv = float(input("FIRST NUMBER : "))
      secondNumberDiv = float(input("SECOND NUMBER : "))
      answer = firstNumberDiv / secondNumberDiv
      print("answer :",answer)
      print("")
      print("Please Enter N to Try anothere problem or Enter Y to exit")
    elif selection == 4:
      firstNumberSqu = float(input("FIRST NUMBER : "))
      secondNumberSqu = float(input("SECOND NUMBER : "))
      answer = firstNumberSqu**secondNumberSqu
      print("answer **",answer)
      print("")
      print("Please Enter N to Try anothere problem or Enter Y to exit")
    elif selection == 5:
      firstNumberMul = float(input("FIRST NUMBER : "))
      secondNumberMul = float(input("SECOND NUMBER : "))
      answer = firstNumberMul*secondNumberMul
      print("answer **",answer)
      print("")
      print("Please Enter N to Try anothere problem or Enter Y to exit")
    else:
      print("The Number You Have Enterd is INCORRECT, Please Try Again With A Valid Number")
      print("")
      print("Please Enter N to Try anothere problem or Enter Y to exit")
  
    exit = input("Y/N : ")
    if exit == "N":
      os.system("cls")
    else:
        os.system("cls")
        break

# Guess the number game

def GuessNumber():
  counter = 0
  correct_number = random.randint(1,10)

  print(" ===== GUESS A NUMBER 1-10 =====")
  while True:
      guess = int(input("Guess : "))
      if guess < 0:
          print("YOU CAN GO BELOW 0")
          exit()
      elif guess < correct_number:
          print("That number is too low, try again")
          counter += 1
      elif guess > correct_number:
          print("that number is too high!, try again")
          counter += 1
      elif guess == correct_number:
          print("CORRECT!")
          print("it took you", counter,"trys")
          time.sleep(5)
          os.system("cls")
          break

# Infinit Sided Dice

def infDice():
  print(" ===== Infinite sided dice =====")

  sides = int(input("How many sides? : "))
  playgame = "yes"

  def diceRoll(sides):
    print("You rolled a", random.randint(1,sides))

  while True: 
    diceRoll(sides)
    playOrExit = input("type anything to leave : ")
    if playOrExit == 1:
      print("you rolled a",diceRoll(sides))
      os.system("cls")
      break
    else:
      os.system("cls")
      break

# Simple charecter creator
def CharCreate():
  while True:
    def diceroll():
      import random
      rolldice = random.randint(1,100)
      return rolldice
    
    health = diceroll()
    
    print(" ===== charactor creator =====")
    print("I will ask a few questions that will be put together into a character")
    
    name = input(" 1 : what is the character's name? : ")
    weapon = input(" 2 : What weapon does this character use? : ")
    specialABL = input("3 : Last question, What special ability does this character use? : ")
    print("")
    print("===== CHARACTER STATS =====")
    print("")
    print("NAME : ", name)
    print("")
    print("WEAPON : ", weapon)
    print("")
    print("SPECIAL ABILITY : ", specialABL)
    print("")
    print(" ===== HEALTH :", health,"=====")
    
    exit = input("TYPE ANYTHING TO EXIT : ")
    if exit == "f":
      os.system("cls")
      break
    else:
      os.system("cls")
      break

# ===== Char Battler =====
def CharacterBattler():
  while True:
    def rollDice(side):
      result = random.randint(1,side)
      return result

    def health():
      healthStat = ((rollDice(6)*rollDice(12))/2)+10
      return healthStat

    def strength():
      strengthStat = ((rollDice(6)*rollDice(8))/2)+12
      return strengthStat


    print("⚔️ BATTLE TIME ⚔️")
    print()
    c1Name = input("Name your Legend:\n")
    c1Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
    print()
    print(c1Name)
    c1Health = health()
    c1Strength = strength()
    print("HEALTH:", c1Health)
    print("STRENGTH:", c1Strength)
    print()
    print("Who are they battling?")
    print()

    c2Name = input("Name your Legend:\n")
    c2Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
    print()
    print(c2Name)
    c2Health = health()
    c2Strength = strength()
    print("HEALTH:", c2Health)
    print("STRENGTH:", c2Strength)
    print()

    round = 1
    winner = None

    while True:
      time.sleep(1)
      os.system("clear")
      print("⚔️ BATTLE TIME ⚔️")
      print()
      print("The battle begins!")

      c1Dice = rollDice(6)
      c2Dice = rollDice(6)

      difference = abs(c1Strength - c2Strength) + 1

      if c1Dice > c2Dice:
        c2Health -= difference
        if round==1:
          print(c1Name, "wins the first blow")
        else:
          print(c1Name, "wins round", round)
      elif c2Dice > c1Dice:
        c1Health -= difference
        if round==1:
          print(c2Name, "wins the first blow")
        else:
          print(c2Name, "wins round", round)
      else:
        print("Their swords clash and they draw round", round)

      print()
      print(c1Name)
      print("HEALTH:", c1Health)
      print()
      print(c2Name)
      print("HEALTH:", c2Health)
      print()

      if c1Health<=0:
        print(c1Name, "has died!")
        winner = c2Name
        break
      elif c2Health<=0:
        print(c2Name, "has died!")
        winner = c1Name
        break
      else:
        print("And they're both standing for the next round")
        round += 1
        

      time.sleep(1)
      os.system("clear")
      print("⚔️ BATTLE TIME ⚔️")
      print()
      print(winner, "has won in", round, "rounds")
      playagain = input(" ===== Y = EXit / N = PLAY AGAIN =====")
      if playagain == "N":
        os.system("cls")
        continue
      else:
        os.system("cls")
        break
    
# ===== main title select =====

while True:
  time.sleep(1)
  print(" ===== Sam's Python tools and othere stuff =====")
  time.sleep(0.2)
  print(" 1 : Calculator")
  time.sleep(0.2)
  print(" 2 : Guess Number Game")
  time.sleep(0.2)
  print(" 3 : Infinit Sided Dice")
  time.sleep(0.2)
  print(" 4 : Charactor Creator")
  time.sleep(0.2)
  print(" 5 : Charactor Battler")
  time.sleep(0.2) 
  print(" 6 : Coming soon...")
  select = int(input("Select : "))
  if select == 1:
    os.system("cls")
    calcu()
  elif select == 2:
    os.system("cls")
    GuessNumber()
  elif select == 3:
    os.system("cls")
    infDice()
  elif select == 4:
    os.system("cls")
    CharCreate()
  elif select == 5:
    os.system("cls")
    CharacterBattler()
  elif select == 6:
    print("Coming soon...")
    time.sleep(2)
    os.system("cls")
    continue
  else:
    time.sleep(3)
    os.system("cls")
    continue
  