from side import accelerate_electron, accelerate_proton, accelerate_neutron

def create_matrix(size):
    return [[1 for _ in range(size)] for _ in range(size)]

def cyclotron(matrix, particle=None):

    if particle is None:
        return matrix


    if particle == "e":
        return accelerate_electron(matrix)
    elif particle == "p":
        return accelerate_proton(matrix)
    elif particle == "n":
        return accelerate_neutron(matrix)
    

    
