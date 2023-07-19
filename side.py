
def create_matrix(size):
    return [[1 for _ in range(size)] for _ in range(size)]

def accelerate_electron(matrix):
    size = len(matrix)

    for i in range(size):
        matrix[0][i] = "e"
        matrix[i][0] = "e"

    return matrix

def accelerate_proton(matrix):

    size = len(matrix)

    for i in range(size):
        if i == 0 or i == size - 1:
            matrix[i][i] = "p"
        else:
            matrix[i][1] = "p"
            matrix[1][i] = "p"

    return matrix



def accelerate_neutron(matrix):
    size = len(matrix)

    for i in range(size):
        for j in range(size):
            if i == 0:
                matrix[i][j] = "n"
            else:
                matrix[i][j] = 1

    return matrix