def decor_calc(func):
    def wrapper(*args):
        first = args[0]
        second = args[1]
        if first == second:
            return func(first, second, "+")
        elif first < 0 or second < 0:
            return func(first, second, "*")
        elif first > second:
            return func(first, second, "-")
        elif first < second:
            return func(first, second, "/")

    return wrapper


@decor_calc
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "*":
        return first * second
    elif operation == "-":
        return first - second
    elif operation == "/":
        return first / second


print('Равны:', calc(1, 1))
print('первое больше второго:', calc(10, 5))
print('второе больше первого', calc(5, 10))
print('одно из чисел отрицательное', calc(-10, 5))
