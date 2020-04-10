'''
    Util function for reading a graph represented as a adjacency matrix
'''
def read_graph(fileName):
    f = open(fileName, "r")
    n = int(f.readline())
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elements = line.split(",")
        for e in elements:
            mat[i].append(int(e))
    f.close()
    return n, mat


def read_parameters(file_name):
    f = open(file_name, "r")
    line = f.readline()
    population_dimension = int(line)
    line = f.readline()
    number_of_parents = int(line)
    line = f.readline()
    tournament_dimension = int(line)
    line = f.readline()
    mutation_ratio = float(line)
    line = f.readline()
    number_of_steps = int(line)
    f.close()
    return population_dimension, number_of_parents, tournament_dimension, mutation_ratio, number_of_steps
