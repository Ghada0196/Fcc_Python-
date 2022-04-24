class Category:

  name = ''

  def __init__(self, name):
    self.name = name
    ledger = list()
    self.ledger = ledger
    
  
  def deposit(self, amount, description = ''):
    obj = dict()
    obj["amount"] = amount
    obj["description"] = description
    self.ledger.append(obj)

  def get_balance(self):
    total = 0
    for i in range(len(self.ledger)):
      total += self.ledger[i]["amount"]
    return total

  def check_funds(self, amount):
    balance = self.get_balance()
    if amount > balance:
      return False
    else:
      return True

  def withdraw(self, amount, description = ''):
    if self.check_funds(amount):
      self.deposit(amount * -1 , description)
      return True
    else:
      return False

  def transfer(self, amount, another):
    if self.check_funds(amount):
      desc = "Transfer to " + another.name
      self.deposit(amount * -1, desc)
      desc = "Transfer from " + self.name
      another.deposit(amount, desc )
      return True
    else:
      return False

  def __str__(self):
    n = round((30 - len(self.name)) / 2)
    display = '*' * (30 - len(self.name) - n) + self.name + '*' * n + '\n'
    for i in range(len(self.ledger)):
      na= len("%.2f" % self.ledger[i]["amount"])
      nd = len(self.ledger[i]["description"])
      if nd >= 23:
        display += self.ledger[i]["description"][ :23]
      else:
        display += self.ledger[i]["description"] + ' '* (23 - nd)
      display += ' ' * (7 - na) + "%.2f" % self.ledger[i]["amount"] + '\n'
    display += "Total: " + str(self.get_balance())
    return display

def create_spend_chart(categories):

  spent = list() #cotains amounts spent by each category
  x = list() #contains lengths of names of categories
  t = 0 #total of all amounts spent of all categories
  n =len(categories)

  for i in range(n):
    x.append(len(categories[i].name))
    for j in categories[i].ledger:
      if j["amount"] < 0:
        spent.append(j["amount"] * -1)
        t += j["amount"] * -1
    
  display = "Percentage spent by category\n"
  i = 100
  while i >= 0:
    if i == 100:
      display += str(i) + '|'
    elif i == 0:
      display += '  ' + str(i) + '|'
    else:
      display += ' ' + str(i) + '|'

    for j in range(n):
      if int(spent[j] / t * 10) >= i/10:
        display += ' o '
      else:
        display += '   '
    display += ' \n'
    i = i - 10
 
  display += '    ' + '-' *(n * 3 + 1) + '\n'
    
  longest = max(x)
  for i in range(longest):
    display += '    '
    for j in range(n):
      if i < x[j]:
        display += ' ' + categories[j].name[i] + ' '
      else:
        display += '   '
    display += ' \n'
    
  return display[:len(display) - 1]