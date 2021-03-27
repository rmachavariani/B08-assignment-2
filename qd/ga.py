from qd.map_points import *
import random

airport_array = getAirports()

def makeNewPopulation(population, elite_size, mutation_rate):
    selection = []
    mating_pool = []
    children = []
    mutated_population = []

    fitness_array = ranking(population)

    fitness_percentage = (np.cumsum(fitness_array[:,1]) / np.sum(fitness_array[:,1])) * 100

    for i in range(elite_size):
        selection.append(fitness_array[i][0])
    for i in range(len(fitness_array) - elite_size):
        pick = 100 * random.random()
        for i in range(len(fitness_array)):
            if pick <= fitness_percentage[i]:
                selection.append(fitness_array[i][0])
                break
    for i in range(len(selection)):
        mating_pool.append(population[int(selection[i])])

    random_pool = random.sample(mating_pool, len(mating_pool))

    for i in range(elite_size):
        children.append(mating_pool[i])

    for i in range(len(mating_pool) - elite_size):
        children.append(breeding(random_pool[i], random_pool[len(mating_pool) - i - 1]))

    for i in range(len(population)):
        mutated = mutate(population[i], mutation_rate)
        mutated_population.append(mutated)

    return mutated_population


def geneticAlgorithm(airport_array, population_size, elite_size, mutation_rate, generations_qty):
    population = []
    for i in range(population_size):
        route = random.sample(airport_array, len(airport_array))
        population.append(route)

    for i in range(generations_qty):
        population = makeNewPopulation(population, elite_size, mutation_rate)

    final_ranking = ranking(population)
    winner = population[int(final_ranking[0][0])]
    for airport in winner:
        print(airport.code)

def ranking(population):
    fitness_array = []
    for i in range(len(population)):
        fitness_array.append([i, Fitness(population[i]).routeFitness()])

    fitness_array = np.array(fitness_array)
    return fitness_array[fitness_array[:, 1].argsort()]


def breeding(parent1, parent2):
    geneA = random.choice(range(len(parent1)))
    geneB = random.choice([i for i in range(len(parent1)) if i not in [geneA]])
    child_from_parent1 = []

    for i in range(min(geneA, geneB), max(geneA, geneB)):
        child_from_parent1.append(parent1[i])

    child_from_parent2 = [i for i in parent2 if i not in child_from_parent1]

    child = child_from_parent1 + child_from_parent2
    print(len(parent1),len(child))

    return child


def mutate(route, mutation_rate):
    for i in range(len(route)):
        if (random.random() < mutation_rate):
            i2 = random.choice([index for index in range(len(route)) if index not in [i]])
            airport1 = route[i]
            airport2 = route[i2]

            route[i] = airport2
            route[i2] = airport1
    return route

pop = geneticAlgorithm(airport_array, 100, 20, 0.01, 500)
