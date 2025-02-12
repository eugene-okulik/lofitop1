def finish_me(func):
    def wrapper():
        print('print me')
        func()
        print('finished')
    return wrapper


@finish_me
def calk():
    print(2 + 2)

calk()
