import random


def position(number, title, column):
    print(title)
    students = list(range(1, number + 1))

    random.shuffle(students)
    pos = ""

    for i in range(0, number):
        if students[i] < 10:
            pos += " "
        pos += str(students[i]) + " "
        if (i + 1) % column == 0:
            pos += "\n"

    print(pos)


position(22, "2-10", 6)
