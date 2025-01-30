import sys
sys.set_int_max_str_digits(1000000)


def fibgenerator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibgenerator()
i = 0
for num in fib_gen:
    if i == 5:
        print("5-е =", num)
    if i == 200:
        print("200-е =", num)
    if i == 1000:
        print("1000-е =", num)
    if i == 100000:
        print("100000-е =", num)
        break
    i += 1
