import os

class remover:
    def __init__(self, path):
        self.path = path

    def remove(self):
        os.remove(self.path)
        print(f"{self.path} 파일이 삭제되었습니다.\n")
        return
