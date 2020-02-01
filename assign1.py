def mainMenu():

#Accept upper-case/lower-case input and leading/trailing spaces
  def formatInput(textLine) :
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = " ".join(wordList)
    return textLine

#Input for program by defining the inputs and is only called when that function is executed
  def Eggs():
    a = input("How many Eggs would you like?")
    if a.isnumeric() == True:       #Validate if input is numeric
      return a
    else:
      print("Enter a valid number")
  def Bacon():
    b = input("How many strips of Bacon would you like?")
    if b.isnumeric() == True:
      return b
    else:
      print("Enter a valid number")
  def Sausage():
    c = input("How many strips of Sausage would you like?")
    if c.isnumeric() == True:
      return c
    else:
        print("Enter a valid number")
  def Hashbrown():
    d = input("How many pieces of Hashbrown would you like?")
    if d.isnumeric() == True:
      return d
    else:
      print("Enter a valid number")
  def Toast():
    e = input("How many pieces of Toast would you like?")
    if e.isnumeric() == True:
      return e
    else:
      print("Enter a valid number")
  def Coffee():
    f = input("How many cups of Coffee would you like?")
    if f.isnumeric() == True:
      return f
    else:
      print("Enter a valid number")
  def Tea():
    g = input("How many Tea bags would you like?")
    if g.isnumeric() == True:
      return g
    else:
      print("Enter a valid number")

#Constant price of all items on menu
  PRICE_PER_EGG = 0.99
  PRICE_PER_BACON = 0.49
  PRICE_PER_SAUSAGE = 1.49
  PRICE_PER_HASHBROWN = 1.19
  PRICE_PER_TOAST = 0.79
  PRICE_PER_COFFEE = 1.09
  PRICE_PER_TEA = 0.89

#price that is calculated in the final costs when it is NOT called upon by user
  eggs = 0
  bacon = 0
  sausage = 0
  hashbrown = 0
  toast = 0
  coffee = 0
  tea = 0

#Loop to keep program running until terminated by user
  finished = False
  while not finished:
    item = input("Enter item (q to terminate): eggs, bacon, sausage, hash brown, toast, coffee, tea: ")
    item = formatInput(item)
    if item in {"eggs", "bacon", "sausage", "hashbrown", "toast", "coffee", "tea", "q"}:
      if item == "q":
        finished = True
      if not finished:
        if item == 'eggs':
          eggs = Eggs()
        elif item == "bacon":
          bacon = Bacon()
        elif item == "sausage":
          sausage = Sausage()
        elif item == "hashbrown":
          hashbrown = Hashbrown()
        elif item == "toast":
          toast = Toast()
        elif item == "coffee":
          coffee = Coffee()
        elif item == "tea":
          tea = Tea()
    else:
      print("Please enter a valid selection")

#Code to calculate various costs
  PreTax = (eggs*PRICE_PER_EGG + bacon*PRICE_PER_BACON + sausage*PRICE_PER_SAUSAGE + hashbrown*PRICE_PER_HASHBROWN + toast*PRICE_PER_TOAST + coffee*PRICE_PER_COFFEE + tea*PRICE_PER_TEA)

  Tax = (eggs*PRICE_PER_EGG + bacon*PRICE_PER_BACON + sausage*PRICE_PER_SAUSAGE + hashbrown*PRICE_PER_HASHBROWN + toast*PRICE_PER_TOAST + coffee*PRICE_PER_COFFEE + tea*PRICE_PER_TEA)*0.13

  total = (eggs*PRICE_PER_EGG + bacon*PRICE_PER_BACON + sausage*PRICE_PER_SAUSAGE + hashbrown*PRICE_PER_HASHBROWN + toast*PRICE_PER_TOAST + coffee*PRICE_PER_COFFEE + tea*PRICE_PER_TEA)*1.13

#Print final costs
  print("Cost: $%.2f" %(PreTax))
  print("Tax: $%.2f" %(Tax))
  print("Total: is $%.2f" %(total))

mainMenu()
