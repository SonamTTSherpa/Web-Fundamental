class user:
    def __init__(self,username,email_address):
        self.name=username
        self.email=email_address
        self.account_balance=0
    def make_deposit(self,amount):
        self.account_balance +=amount
    def make_withdrawl(self,amount):
        self.account_balance -=amount
    def display_user_balance(self):
        print(self.account_balance)

        guido=user("Guido Van Rossum","guido@python.com")
        monty=user("Monty Python","monty@python.com")
        sonam=user("Sonam Sherpa","sonam@python.com")

        guido.make_deposit(100)
        guido.make_deposit(200)
        guido.make_deposit(100)
        guido.make_withdrawl(100)

        guido.display_user_balance()

        monty.make_deposit(50)
        monty.make_deposit(50)
        monty.make_withdrawl(25)
        monty.make_withdrawl(25)

        monty.display_user_balance()

        sonam.make_deposit(500)
        sonam.make_withdrawl(100)
        sonam.make_withdrawl(100)
        sonam.make_withdrawl(100)

        sonam.display_user_balance()