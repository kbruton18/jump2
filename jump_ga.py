import random
import math

from dna import dna


population = []
num_generations = 300
population_size = 100

# append the individuals for the initial population
for x in range(0, population_size):
	population.append(dna())

# iterates the number of generations
for x in range(0, num_generations):
	# iterates through the indvidiuals in population so that each goes through cross over
	# and mutation, creates a child population
    children_pop = []

    for individual in range(0, population_size):
        population[individual].evaluate()

    population.sort(key=lambda f:f.fitness, reverse=True)
    best = population[0]

    print x, population[0].fitness

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

	# create a new population and fill it with the 25
    new_population = []
    for x in range(0, population_size/2):
        new_population.append(population[individual])
        new_population.append(random.choice(children_pop))


	# sort new population and keep track of the best player


from jumpmain import game_function
ann = best.copyNeuron()
print game_function(ann, True)


