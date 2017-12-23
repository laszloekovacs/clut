# classes n objects
# double _ are __private
# self = this in other lang


class Person:
    __name = ''
    __email = ''

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def set_email(self, mail):
        self.__email = mail

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def toString(self):
        return '{} can be reached at {}'.format(self.__name, self.__email)


brad = Person('brad', 'brad@mail.com')
brad.set_name('mike')
print(brad.toString())


# inheritance
class Customer(Person):

    balance = 0

    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.balance = balance

    def get_balance(self):
        return self.balance

    def toString(self):
        print('{} has a balance of {}'.format(self.__name, self.balance))

    def set_balance(self, bal):
        self.balance = bal


# playing with the customers
kate = Customer('kate', 'kate@mail.com', 400)

print(kate.toString())
