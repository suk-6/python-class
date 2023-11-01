from fileReader import reader

class writer:
    def __init__(self, path, data):
        self.path = path
        self.data = data

    def write(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(self.data)
        print(f"변경된 파일 내용: {reader(self.path).read()}\n")
