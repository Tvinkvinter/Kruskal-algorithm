class Matrix:
    def __init__(self, n, m, unit_m=False):
        self.n = n
        self.m = m
        self.matrix = []
        for i in range(n):
            self.matrix.append([])
            for j in range(m):
                if j == i and unit_m:
                    self.matrix[i].append(1)
                else:
                    self.matrix[i].append(0)


def matrix_from_file(file_name):
    f = open(file_name, 'r')
    nm = f.readline().split()
    n = int(nm[0])
    m = int(nm[1])
    mat = Matrix(n, m)
    rows = f.readlines()[0:]
    for i in range(n):
        for j in range(m):
            mat.matrix[i][j] = int(rows[i].split()[j])
    return mat
