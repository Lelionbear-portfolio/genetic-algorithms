"""
This is considered as the `Hello World` of genetic algorithm framework
"""
from deap import base, creator, tools
import matplotlib.pyplot as plt
import seaborn as sns
import random

# constants
ONE_MAX_LEN = 100       # length of bit string to be optimized

# GenAlgo constants
POPULATION_SIZE = 200   # num of individuals in population
P_CROSSOVER = 9.0       # probability for crossover 
P_MUTATION = 0.1        # probability for mutating an individual
MAX_GENERATIONS = 50    # max num of generations for stopping condition

RANDOM_SEED = 42            # When experimenting with the code, we may want to be able to run the same experiment several times and get repeatable results
random.seed(RANDOM_SEED)    # To accomplish this, we set the random function seed to a constant number of some value

toolbox = base.Toolbox()
toolbox.register('zeroOrOne', random.randint, 0, 1) # registered new function

creator.create('FitnessMax', base.Fitness, weights=(1.0,))  # fitness class goal is to maximize it, using a weights tuple with single positive weight

creator.create('Individual', list, fitness=creator.FitnessMax)  # individual class: container type in which the resulting objects will be placed

toolbox.register('individualCreator', tools.initRepeat, creator.Individual, toolbox.zeroOrOne, ONE_MAX_LEN) # creates a single individual

toolbox.register('populationCreator', tools.initRepeat, list, toolbox.individualCreator)    # creates a list of individuals

def oneMaxFitness(individual):
    return sum(individual), # return a tuple

toolbox.register('evaluate', oneMaxFitness)

toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=1.0/ONE_MAX_LEN) # indpb === independant probability


def main():
    print('Starting One Max Problem Version 1')

    population = toolbox.populationCreator(n=POPULATION_SIZE)
    generationCounter = 0

    fitnessValues = list(map(toolbox.evaluate, population))

    for individual, fitnessValue in zip(population, fitnessValues):
        individual.fitness.values = fitnessValue

    fitnessValues = [individual.fitness.values[0] for individual in population]

    maxFitnessValues = []
    meanFitnessValues = []

    while max(fitnessValues) < ONE_MAX_LEN and generationCounter < MAX_GENERATIONS: # stopping conditions
        generationCounter+=1

        offspring = toolbox.select(population, len(population))
        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < P_CROSSOVER:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values
            
        for mutant in offspring:
            if random.random() < P_MUTATION:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        
        freshIndividuals = [ind for ind in offspring if not ind.fitness.valid]  # ind === individual
        freshFitnessValues = list(map(toolbox.evaluate, freshIndividuals))
        for individual, fitnessValue in zip(freshIndividuals, freshFitnessValues):
            individual.fitness.values = fitnessValue

        population[:] = offspring
        fitnessValues = [ind.fitness.values[0] for ind in population]

        maxFitness = max(fitnessValues)
        meanFitness = sum(fitnessValues) / len(population)
        maxFitnessValues.append(maxFitness)
        meanFitnessValues.append(meanFitness)

        print('- Generation {}: Max Fitness = {}, Avg Fitness = {}'.format(generationCounter, maxFitness, meanFitness))

        best_index = fitnessValues.index(max(fitnessValues))
        print('Best Individual = ', *population[best_index], '\n')

    sns.set_style("whitegrid")
    plt.plot(maxFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Generation')
    plt.ylabel('Max / Average Fitness')
    plt.title('Max and Average fitness over Generations')
    plt.show()



if __name__ == '__main__':
    main()
