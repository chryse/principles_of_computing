val1 = [1, 2, 3]
val2 = val1[1:]
val1[2] = 4
#print val2[1]

def appendsums(lst):
    sum = 0
    for i in range(25):
        sum = lst[len(lst) -1] + lst[len(lst) -2] + lst[len(lst) -3]
        #print sum
        lst.append(sum)
    return lst

sum_three = [0, 1, 2]
appendsums(sum_three)
#print sum_three[10]
print sum_three[20]

class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.initial_balance = initial_balance
        self.total_fee = 0
   
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.initial_balance += amount
        return self.initial_balance 
    
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.initial_balance -= amount
        if self.initial_balance < 0:
            self.initial_balance -= 5
            self.total_fee += 5
        return self.initial_balance
    
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.initial_balance
        
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.total_fee
    
#my_account = BankAccount(10)
#my_account.withdraw(15)
#my_account.deposit(20)
#print my_account.get_balance(), my_account.get_fees()
        
my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5) 
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50) 
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
print my_account.get_balance(), my_account.get_fees()


#print {1: 'a', (5, 'item'): [100], 'key': {True: 'hello', -9: 0}}
print {1: 'a', (5, 'item'): [100], 'key': {True: 'hello', -9: 0}, "": 1, None: 20, False: 30}

def clock_helper(total_seconds):
    """
    Helper function for a clock
    """
    seconds_in_minute = total_seconds % 60
    
clock_helper(90)

board = []
ROW = 5
COL = 5

for x in range(4):
    board.append([0] * ROW)

def print_board(board):
    for fillO in board:
        print " ".join(fillO)

b = []
for i in range(4):
    for j in range(4):
        b.append([i, j])
    
print b    