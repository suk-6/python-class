class reader:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            return f.read()
