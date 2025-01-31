import random

salary = int(input('Укажите вашу Salary: '))
print(salary)
bonus = bool(random.randint(0, 1))
print(bonus)
if bonus is True:
    bonus_new = random.randint(0, 1000)
    print(f"{salary}, {bonus} - '${salary + bonus_new}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
