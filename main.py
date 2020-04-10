import copy

from genetic_alg import generate_population, selection, crossover, mutation, survival_selection, fitness
from reader import read_parameters, read_graph

'''
fitness:
    - minimal distance
    
reproduction selection:
    - tournament selection

crossover:
    - ordered crossover
    
mutation:
    - swap
    - point mutation
 
survival selection:
    - elitist selection

input parameters:
1. population_dimension
2. number_of_parents ( the number of selected chromosome for crossover )
3. tournament_dimension ( the number of selected chromosome for crossover )
4. mutation_ratio ( the probability of a chromosome to be affected by mutation )
5. number_of_steps ( stop condition )
'''


def main():
    #  input_graph = read_graph("input/225-1/easy_03_tsp.txt")
    #  input_graph = read_graph("input/225-1/medium_01_tsp.txt")
    input_graph = read_graph("input/225-1/hard_02.txt")

    no_nodes = input_graph[0]
    network = input_graph[1]

    print no_nodes
    print network
    params = read_parameters("input/parameters.txt")

    population_dimension = params[0]
    number_of_parents = params[1]
    tournament_dimension = params[2]
    mutation_ratio = params[3]
    number_of_steps = params[4]

    population = generate_population(population_dimension, no_nodes, network)

    # assign a random chromosome to be the best
    overall_best = population[0]
    overall_best_fitness = fitness(population[0], network)
    for step in range(number_of_steps):
        fathers = selection(population, number_of_parents, tournament_dimension, network)
        mothers = selection(population, number_of_parents, tournament_dimension, network)
        children = crossover(fathers, mothers)
        population = population + children
        population = mutation(population, mutation_ratio, no_nodes)
        population = survival_selection(population, network, population_dimension)
        best = min(population, key=lambda x: fitness(x, network))
        best_fitness = fitness(best, network)
        if overall_best_fitness > best_fitness:
            print "new BEST at step {}".format(step)
            print 'best solution = {}'.format(best)
            print 'best fitness = {}'.format(best_fitness)
            print ""
            overall_best = copy.deepcopy(best)
            overall_best_fitness = best_fitness

    print 'overall best = {}'.format(overall_best)
    print 'overall best fitness= {}'.format(overall_best_fitness)


if __name__ == "__main__":
    main()
