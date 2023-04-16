def f1():
    print("123\n456")

def f2():
    a = "ab"
    print("%5s" % a)

def f3():
    krw = float(input("원화를 입력하세요: "))
    usd = float(input("환율을 입력하세요: "))

    print("원화 %.2f원은 달러로 %.2f달러입니다." % (krw, krw/usd))

def f4():
    a = "abcdef"
    print(a[-1:])

def f5():
    a = "abcdef"
    print(len(a))
