from deap import base, creator, tools, algorithms
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
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
    print('Starting One Max Problem Version 2')

    population = toolbox.populationCreator(n=POPULATION_SIZE)
    # generationCounter = 0

    # prepare the statistics object:
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("max", np.max)
    stats.register("avg", np.mean)

    # perform the Genetic Algorithm flow:
    population, logbook = algorithms.eaSimple(population, 
                                              toolbox, 
                                              cxpb=P_CROSSOVER, 
                                              mutpb=P_MUTATION, 
                                              ngen=MAX_GENERATIONS, 
                                              stats=stats, 
                                              verbose=True)


    # Genetic Algorithm is done - extract statistics:
    maxFitnessValues, meanFitnessValues = logbook.select("max", "avg")

    sns.set_style("whitegrid")
    plt.plot(maxFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Generation')
    plt.ylabel('Max / Average Fitness')
    plt.title('Max and Average Fitness over Generations')
    plt.show()


if __name__ == "__main__":
    main()