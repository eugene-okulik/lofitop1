line1 = "результат операции: 42"
line2 = "результат операции: 514"
line3 = "результат работы программы: 9"
line4 = "результат: 2"
def slozhenie(line):
    number = int(line.split(': ')[1])
    return number + 10
print(slozhenie(line1))
print(slozhenie(line2))
print(slozhenie(line3))
print(slozhenie(line4))