
class Employee:
    raise_amnt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first.lower() + '.' + self.last.lower() + '@company.com'

    def __repr__(self):
        return "Employee(" + self.first + ", " + self.last + ", " + str(self.pay) + ")"

    def __str__(self):
        return self.first + " " + self.last + " has email " + self.email + " and earns " + str(self.pay)

    def give_raise(self):
        self.pay *= self.raise_amnt

class Developer(Employee):
    raise_amnt = 1.1
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


def main():
    emp1 = Employee('Anna', 'Jones', 55000)
    emp2 = Employee('Bob', 'Smith', 47000)
    print(emp1)
    print(emp2)
    emp1.give_raise()
    print(emp1)
    dev1 = Developer('Sara', 'Andersen', 59000, 'Python')
    print(dev1)
    dev1.give_raise()
    print(dev1)
    print(isinstance(emp1, Employee))

    
if __name__ == '__main__':
    main()