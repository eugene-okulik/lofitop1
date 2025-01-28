number = 7

while True:
    user_guess = int(input("Угадайте цифру от 0 до 9: "))
    if user_guess == number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова")
