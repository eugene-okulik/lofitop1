chisla = range(1, 101)
for chislo in chisla:
    if chislo % 3 == 0 and chislo % 5 != 0:
        print("fuzz")
    elif chislo % 5 == 0 and chislo % 3 != 0:
        print('buzz')
    elif chislo % 3 == 0 and chislo % 5 == 0:
        print("FuzzBuzz")
    else:
        print(chislo)
