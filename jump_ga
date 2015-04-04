population = []
num_generations = 300
population_size = 100

# append the individuals for the initial population
for x in range(0, population_size):
	population.append( dna() )

# iterates the number of generations
for x in range(0, num_generations):
	# iterates through the indvidiuals in population so that each goes through cross over
	# and mutation, creates a child population
	for individual in range of(0, population_size):
		individual.evaluate()
		# create empty new population
		children_pop = []
		chance = random.random()
		if chance < .7
			# cross over for parents
			parent_one = random.randint(0, population_size)
			parent_two = random.randint(0, population_size)
			new_child = population[parent_one].crossover(population[parent_two])
			children_pop.append(new_child)
		else 
			# mutation
			mutated_child = mutate(population[x])
			children_pop.append(mutated_child)
	# sort children and parent population by best at top
	children_pop.sort(key=lambda x:x.fitness,reverse=True) 
	population.sort(key=lambda x:x.fitness, reverse=True)

	# create a new population and fill it with the 25
	new_population = []
	for x in range(0, population_size/4)
		new_population.append(children_pop[x])
		new_population.append(population[x])
	for x in range(0, population_size/4)
		random_index = random.randint(0, population_size)
		new_population.append(children_pop[x])
		new_population.append(population[x])
	# sort new population and keep track of the best player
	new_population.sort(key=lambda, x:x.fitness, reverse=True)
	best = new_population[0]

from jump import game
ann = best.copyNeuron()
print game(ann, True)
