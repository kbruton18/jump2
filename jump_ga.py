import random
import math

from dna import dna


population = []
num_generations = 50
population_size = 20


# append the individuals for the initial population
for x in range(0, population_size):
	population.append(dna())

best = None

# iterates the number of generations
for x in range(0, num_generations):
	# iterates through the indvidiuals in population so that each goes through cross over
	# and mutation, creates a child population
    children_pop = []

    for individual in range(0, population_size):
        population[individual].evaluate()

        chance = random.random()

        if chance < .85:
		# cross over for parents
		    parent_one = random.choice(population)
		    parent_two = random.choice(population)
		    new_child = parent_one.crossover(parent_two)
		    children_pop.append(new_child)
        else:
		# mutation
		    mutated_child = population[individual].mutate()
		    children_pop.append(mutated_child)


    population.sort(key=lambda f:f.fitness, reverse=True)

    best = population[0]

    print x, population[0].fitness


    # evaluate children
    for individual in range(0, population_size):
        children_pop[individual].evaluate()

    children_pop.sort(key=lambda f:f.fitness, reverse=True)

	# create a new population and fill it with the 20 best ones from parents and 20 best ones from children
    new_population = []


    for x in range(0, int(0.1 * population_size)):
        new_population.append(population[x])
        new_population.append(children_pop[x])
    for x in range(0, int(0.4 * population_size)):
        new_population.append(random.choice(children_pop))
        new_population.append(random.choice(population))
        #new_population.append(random.choice(children_pop))

    population = new_population

# sort new population and keep track of the best player

from jumpmain import game_function
print best.fitness, '< fitness ', best.weights
ann = best.copyNeuron()
print game_function(ann, True)


