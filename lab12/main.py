class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def add_element(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise IndexError("Індекс поза діапазоном")

    def sum_of_rows(self):
        return [sum(row) for row in self.data]

    def transpose(self):
        transposed_data = [[self.data[row][col] for row in range(self.rows)] for col in range(self.cols)]
        return Matrix.from_list(transposed_data)

    def multiply_by(self, other):
        if self.cols != other.rows:
            raise ValueError("Несумісні матриці для множення")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
        return result

    def is_symmetric(self):
        if self.rows != self.cols:
            return False

        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != self.data[j][i]:
                    return False
        return True

    def rotate_right(self):
        rotated_data = [[self.data[self.rows - 1 - col][row] for col in range(self.rows)] for row in range(self.cols)]
        self.data = rotated_data
        self.rows, self.cols = self.cols, self.rows

    def flatten(self):
        return [element for row in self.data for element in row]

    def diagonal(self):
        if self.rows != self.cols:
            raise ValueError("Матриця не квадратна")

        return [self.data[i][i] for i in range(self.rows)]

    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        cols = len(list_of_lists[0]) if rows > 0 else 0
        matrix = Matrix(rows, cols)
        matrix.data = list_of_lists
        return matrix

matrix = Matrix(2, 3)
print(matrix.data)

matrix.add_element(1, 2, 10)
print(matrix.data)

matrix.add_element(0, 0, 5)
matrix.add_element(0, 1, 10)
print(matrix.sum_of_rows())

transposed = matrix.transpose()
print(transposed.data)

matrix1 = Matrix(2, 3)
matrix1.add_element(0, 0, 1)
matrix1.add_element(0, 1, 2)
matrix1.add_element(0, 2, 3)

matrix2 = Matrix(3, 2)
matrix2.add_element(0, 0, 1)
matrix2.add_element(1, 0, 2)
matrix2.add_element(2, 0, 3)

result = matrix1.multiply_by(matrix2)
print(result.data)

matrix = Matrix(2, 2)
matrix.add_element(0, 1, 5)
matrix.add_element(1, 0, 5)
print(matrix.is_symmetric())

matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
matrix.rotate_right()
print(matrix.data)

print(matrix.flatten())

list_of_lists = [[1, 2], [3, 4]]
matrix = Matrix.from_list(list_of_lists)
print(matrix.data)

matrix = Matrix(3, 3)
matrix.add_element(0, 0, 1)
matrix.add_element(1, 1, 2)
matrix.add_element(2, 2, 3)
print(matrix.diagonal())
