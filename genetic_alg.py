import copy
import itertools
import math
import random


def fitness(perm, network):
    """
        Returns the distance travelled
    """
    dist = 0
    first = perm[0]
    for i in range(1, len(perm)):
        dist = dist + network[first][perm[i]]
        first = perm[i]
    dist = dist + network[first][perm[0]]
    return dist



def generate_random_label(number, max_value):
    """
    Generates a list o number elements, random generated from 1 to max_value
    """
    list_of_numbers = []
    for x in range(0, number):
        list_of_numbers.append(random.randint(1, max_value))
    return list_of_numbers


def generate_population(population_dimension, max_number, network):
    """
         generates a population of population_dimension number of permutations (numbers from 0 to max_number)
    """
    rez = []
    perm = []
    for i in range(max_number):
        perm.append(i)
    # permutations = list(itertools.permutations(perm))
    # check the result
    # print "minimum = {}".format(min(permutations, key=lambda x:fitness(x, network)))
    # print "minimum fitness = {}".format(fitness(min(permutations, key=lambda x:fitness(x, network)),network))
    for i in range(population_dimension):
        #  r = random.randint(0, math.factorial(int(max_number))-1)
        for j in range(0, 15):
            i_index = random.randint(0, max_number-1)
            j_index = random.randint(0, max_number-1)
            aux = perm[i_index]
            perm[i_index] = perm[j_index]
            perm[j_index] = aux

        r = copy.deepcopy(perm)
        rez.append(r)

    print rez
    return rez


def selection(population, number_of_parents, tournament_dimension, network):
    """
        tournament selection --> get the first number of parents form tournament_dimension chromosomes randomly selected
    """
    # get the tournament participants
    tournament = []
    for i in range(tournament_dimension):
        tournament.append(population[random.randint(0, len(population) - 1)])

    # sort by fitness
    tournament.sort(key=lambda x: fitness(x, network))

    # select the first ones
    selected = []
    for i in range(number_of_parents):
        selected.append(tournament[i])

    return selected


def generate_kids(father, mother):
    child1 = []
    child2 = []
    for _ in father:
        child1.append(-1)
        child2.append(-1)

    # generate sublist interval
    limit1 = random.randint(1, len(father) - 1)
    limit2 = random.randint(1, len(father) - 1)
    start = min(limit1, limit2)
    stop = max(limit1, limit2)

    # transcript the sublist on the new chromosome (on the same position)
    for i in range(start, stop):
        child1[i] = father[i]
        child2[i] = mother[i]

    for i in range(0, len(father)):
        # add remaining genes from mother to child1
        if not child1.__contains__(mother[i]):
            aux = 0
            while child1[aux] != -1:
                aux = aux + 1
            child1[aux] = mother[i]

        # add remaining genes from father to child 2
        if not child2.__contains__(father[i]):
            aux = 0
            while child2[aux] != -1:
                aux = aux + 1
            child2[aux] = father[i]

    return child1, child2


def crossover(fathers, mothers):
    """
        Applies an ordered crossover and returns the children
    """

    children = []
    for i in range(len(fathers)):
        kids = generate_kids(fathers[i], mothers[i])
        children.append(kids[0])
        children.append(kids[1])
    return children


def mutation(population, mutation_ratio, no_nodes):
    """
    generate a Point mutation on the population with mutation_ratio (the probability of a chromosome to be mutated)
    - swap 2 points
    """
    for chromosome in population:
        #  generate a number between 0 and 1 and if it is smaller than the ratio, mutate the chromosome
        ran = random.uniform(0, 1)
        if ran < mutation_ratio:
            # generate 2 random ints number that represents the 2 genes that are swapped
            gene_index1 = random.randint(0, len(chromosome) - 1)
            gene_index2 = random.randint(0, len(chromosome) - 1)
            aux = chromosome[gene_index1]
            chromosome[gene_index1] = chromosome[gene_index2]
            chromosome[gene_index2] = aux

    return population


def survival_selection(population, network, initial_size):
    """
    Perform an elitist selection--> eliminate all chromosomes with big fitness, so that the population returns to
    the main size
    """
    sorted_population = sorted(population, key=lambda x: fitness(x, network), reverse=True)
    i = 0
    while len(population) != initial_size:
        population.remove(sorted_population[i])
        i = i + 1
    return population
