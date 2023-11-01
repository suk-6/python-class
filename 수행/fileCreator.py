class creator:
    def __init__(self, path):
        self.path = path

    def create(self):
        with open(self.path, 'a') as f:
            print(f"{self.path} 파일이 생성되었습니다.\n")
            return
