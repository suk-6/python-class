def hello(msg="안녕하세요"):
    print(msg + "!")


hello("오랜만이에요")
hello("이번주에는 뭐하고 지내셨어요?")


def fn(a, b=[]):
    b.append(a)
    print(b)


fn(5, [1, 2, 3])


def gugudan(dan=2):
    for i in range(1, 10):
        print(dan, "*", i, "=", dan * i)


gugudan(3)
gugudan(2)
