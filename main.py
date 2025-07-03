class BankAccount:
  def __init__(self,name,initial_balance):
    self.name=name
    self.balance=initial_balance
  
  def deposit(self, amount):
    self.balance+=amount
  def withdraw(self, amount):
    self.balance-=amount
  def check_balance(self):
    print('Balance Money: ', self.balance)


b1= BankAccount('irfan',250)
print(b1.name)
print(b1.balance)

b1.deposit(750)
b1.check_balance()
b1.withdraw(500)
b1.check_balance()
