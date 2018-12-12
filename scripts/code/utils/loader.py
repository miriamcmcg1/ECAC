class Loader:
    def __init__(self, path, separator=';'):
        self.path = path
        self.separator = separator
        self.data = []

        self.load_file()            

    def load_file(self):
        import csv
        with open(self.path, 'r') as csvfile:
            spam_reader = csv.reader(csvfile, delimiter=self.separator)
            next(spam_reader, None)  # skip the headers
            for entry in spam_reader:
                self.data.append(entry)
