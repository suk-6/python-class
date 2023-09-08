def star(mark, repeat, space, space_repeat, line):
    for i in range(line):
        str = mark * repeat
        for j in range(2, repeat):
            str = str + ((space) * space_repeat) + (mark * repeat)
        print(str)


star("*", 3, "_", 2, 3)
