def sum(a, b):
    return a + b


t = (2, 3)
# print(sum(*t))


def p(*args):
    str = ""
    for i in args:
        str += i
    print(str)


def p1(space, space_num, *args):
    str = args[0]
    for i in range(1, len(args)):
        str = str + (space * space_num) + args[i]

    print(str)


# p1(" ", 3, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j")


def sum2(*args: int):
    sum = 0
    for i in args:
        sum += i
    return sum


def sum3(a, b):
    return a + b


d = {"a": 3, "b": 2}
# print(sum3(**d))


def p(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


p(a=3, b=2, c=1)
p(a=3, b=2)
p(a=3)
p()
