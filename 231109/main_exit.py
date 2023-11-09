from sys import exit

while True:
    print("종료하려면 exit를 입력하세요")
    uInput = input("> ")
    if uInput == "exit":
        exit()
    else:
        print(uInput + "\n")
