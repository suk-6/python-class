import os
from fileReader import reader
from fileWriter import writer
from fileCreator import creator
from fileRemover import remover

class main:
    def __init__(self):
        self.services = {
            1: "파일 생성",
            2: "파일 읽기",
            3: "파일 쓰기",
            4: "파일 제거"
        }
        self.path = os.getcwd()

        self.menu()

    def input(self, prompt):
        print(prompt)
        return input("> ")

    def menu(self):
        for i in self.services.keys():
            print(f"[{i}] {self.services[i]}\n")
        
        try:
            menu = int(self.input("실행하고 싶은 메뉴 번호를 입력하세요"))
        except:
            print("오류!\n")
            main()

        if menu == 1:
            self.fileManager(1)
        elif menu == 2:
            self.fileManager(2)
        elif menu == 3:
            self.fileManager(3)
        elif menu == 4:
            self.fileManager(4)
        else:
            print("오류!\n")
            return main()

    def fileManager(self, menu):
        file = self.input("파일 이름을 입력하세요")
        path = os.path.join(self.path, file)

        try:
            if menu == 1:
                creator(path).create()
            elif menu == 2:
                print(reader(path).read())
            elif menu == 3:
                data = self.input("파일 내용을 입력하세요")
                writer(path, data).write()
            elif menu == 4:
                remover(path).remove()
        except:
            print("오류!\n")
            
        main()
            


if __name__ == "__main__":
    main()
