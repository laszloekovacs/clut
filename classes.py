# classes n objects
# double _ are __private
# self = this in other lang


class Person:
    'a person'
    personname = ''
    email = ''

    def __init__(self, name, email):
        self.personname = name
        self.email = email

    def set_name(self, name):
        self.personname = name

    def set_email(self, mail):
        self.email = mail

    def get_name(self):
        return self.personname

    def get_email(self):
        return self.email

    def info(self):
        return '{} can be reached at {}'.format(self.personname, self.email)


brad = Person('brad', 'brad@mail.com')
brad.set_name('mike')
print(brad.info())


# inheritance
class Customer(Person):

    balance = 0

    def __init__(self, name, email, balance):
        super().__init__(name, email)
        self.balance = balance

    def get_balance(self):
        return self.balance

    def status(self):
        print(self.personname, ' has a balance of', self.balance)

    def set_balance(self, bal):
        self.balance = bal


# playing with the customers
kate = Customer('kate', 'kate@mail.com', 400)

print(kate.status())
