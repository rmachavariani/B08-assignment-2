from qd.class_def import *
from qd.map_points import *
import random
import pandas as pd

airport_array = getAirports()

def getInitialPopulation(airport_array, population_size):
    population = []
    for i in range(population_size):
        route = random.sample(airport_array, len(airport_array))
        population.append(route)
    return population

def rank(population):
    fitness_array = []
    for i in range(len(population)):
        fitness_array.append([i, Fitness(population[i]).routeFitness()])
    fitness_array = np.array(fitness_array)
    return fitness_array[fitness_array[:, 1].argsort()]

def getMatingPool(population, fitness_array, elite_size):




pop = getInitialPopulation(airport_array, 100)
eanking = rank(pop)
getMatingPool(pop, eanking,10)