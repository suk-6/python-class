def ssal(num, reverse=False):
    if reverse:
        for i in range(num):
            print("*" * (num - i))
    else:
        for i in range(num):
            print("*" * (i + 1))


ssal(5)
ssal(5, reverse=True)


def p(*args):
    str = ""
    for i in args:
        str += i
    print(str)


p("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
p("a")


def myFunc(*args):
    print(args)
