from pip._vendor.distlib.compat import raw_input


class Doll:
    def __init__(self, doll_count, name, price, model):
        self.doll_count = doll_count
        self.name = name
        self.price = price
        self.model = model
    @classmethod
    def from_input(cls):
        return cls(
            int(raw_input('Enter the number of dolls (only one model): \n')),
            raw_input('Name: \n'),
            int(raw_input('Price: \n')),
            raw_input('Model: \n'),
        )
    def get_info(self):
        print("There is {0} dolls {1} in the store. The one of this model {2} costs {3} dollars".format(self.doll_count, self.name, self.model, self.price))

class Parents:
    doll_counter = 0
    child_counter = 0
    def __init__(self, money, name, surname, age, sex):
        self.money = money
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex

    @classmethod
    def from_input(cls):
        return cls(
            int(raw_input('Enter your money: \n')),
            raw_input('Name: \n'),
            raw_input('Surname: \n'),
            int(raw_input('Age: \n')),
            raw_input('Sex: \n'),
        )

    def buy(self, doll):
        if (doll.doll_count -  self.doll_counter < 0 or doll.price * self.doll_counter > self.money):
            print("I cannot buy doll {}".format(doll.name))
        else:
            print("I bought this doll {}".format(doll.name))
            print("It costs {} dollars".format(doll.price))
            self.money -= doll.price
            self.doll_counter += 1
            doll.doll_count -= 1

    def get_info(self):
        print("Hi! I'm {0} {1}. I have {2} dollars to buy a doll for my child.".format(self.name, self.surname, self.money))

    def be_parent(self, child):
        print("{0} {1} is my child!".format(child.name, child.surname))
        self.child_counter += 1

class Child(Parents):
    def buy(self, doll):
        print("I want doll '{}'!".format(doll.name))
        self.doll_counter += 1

    def get_info(self):
         print("Hi! I'm {0} {1}!".format(self.name, self.surname))

    def be_child(self, parent):
        print("{0} {1} is my parent!".format(parent.name, parent.surname))


user = Doll.from_input()
user.get_info()

user2 = Doll.from_input()
user2.get_info()

parent1 = Parents.from_input()
parent1.get_info()
parent1.buy(user)
parent1.buy(user2)

child1 = Child.from_input()
child1.get_info()
child1.buy(user)

parent1.be_parent(child1)
child1.be_child(parent1)

