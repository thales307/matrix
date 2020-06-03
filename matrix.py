class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[y for y in x.split()]
            for x in matrix_string.split('\n')]

    def row(self, index):
        return [int(x) for x in self.matrix[index-1]]

    def column(self, index):
        return [int(x[index - 1]) for x in self.matrix]
        