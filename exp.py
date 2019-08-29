class User:
    def __init__(self, name, email, address=''):
        self.name = name
        self.email = email
        self.address = address
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

    def info(self):
        print(self.name,'\n' ,self.email, '\n',self.balance,'\n',self.address)


billy = User('billy', 'billy@billerson.com')

billy.info()
billy.deposit(300)
billy.info()
billy.withdrawal(100)
billy.info()
billy.address = 'srgsergegr'
billy.info()