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
    print("")
  else:
      break
