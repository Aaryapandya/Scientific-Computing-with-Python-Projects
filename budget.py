class Category:
  ledger = list()
  sum = 0
  name = ""
  res = ""

  def __init__(self, c):
    self.name = c
    self.ledger = list()
    self.sum = 0
    self.res = ""


  def deposit(self, amt, des = ""):
    self.ledger.append({"amount": amt, "description": des})
    self.sum = self.sum + amt
  
  def withdraw(self, amt, des = ""):
    if self.check_funds(amt):
      self.ledger.append({"amount": -amt, "description": des})
      self.sum = self.sum - amt
      return True
    else:
      return False

  def get_balance(self):
    return self.sum

  def transfer(self, amt, cat):
    if self.check_funds(amt):
      des = 'Transfer to ' + cat.name
      self.withdraw(amt, des)
      des = 'Transfer from ' + self.name
      cat.deposit(amt, des)
      return True
    else:
      return False
  
  def check_funds(self, amt):
    if amt > self.sum:
      return False
    else:
      return True

  def __str__(self):
    length = int((30-len(self.name))/2)
    l1 = ("*" * length) + self.name + ("*" * length) + "\n"
    self.res = l1 
    max_len = 0
    for lst in self.ledger:
      v = lst['amount']
      k = lst['description']
      v = format(v, '.2f')
      val = str(v)
      max_len = max(max_len, min(len(k), 23)+len(val))
    
    max_len = max_len + 1

    for lst in self.ledger:
      v = lst['amount']
      k = lst['description']
      v = format(v, '.2f')
      val = str(v)
      self.res = self.res + k[:23] + (" "*(max_len-min(len(k), 23)-len(val))) + val + '\n'
    
    self.res = self.res + "Total: " + str(self.sum)

    return self.res

def create_spend_chart(categories):
  graph = 'Percentage spent by category\n'
  n = len(categories)
  sub_total = dict()
  total = 0
  longest = 0
  for c in categories:
    longest = max(longest, len(c.name))
    sub_total[c.name] = 0
    for l in c.ledger:
      if l['amount']<0:
        sub_total[c.name] = sub_total[c.name] - l['amount']
    
    total = total + sub_total[c.name]

  avg = dict()
  for k,v in sub_total.items():
    avg[k] = v/total*100
    avg[k] = avg[k] - avg[k]%10
  
  i = 100
  while(i>=0):
    if i==100:
      graph = graph + '100| '
    elif i>0:
      graph = graph + ' ' + str(i) + '|' + ' '
    else:
      graph = graph + '  0| '
    for k,v in avg.items():
      if(v>=i):
        graph = graph + 'o  '
      else:
        graph = graph + '   '
    graph = graph + '\n'
    i = i - 10
  
  graph = graph + '    -' + ('---'*n)
  for c in categories:
    c.name = c.name + ' '*(longest - len(c.name))
  i = 0
  while(i<longest):
    graph = graph + '\n     '
    for c in categories:
      graph = graph + c.name[i] + '  '
    i = i + 1

  return graph
