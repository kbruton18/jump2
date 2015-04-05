import random
import jumpmain

class dna:
    weights_size = 3

    def __init__(self):
        #randomly assign weights in range -5.0 to 5.0
        self.weights = [random.uniform(-5.0, 5.0), random.uniform(-2.0, 2.0), random.uniform(-5.0, 5.0)]

    def mutate(self):
        # create a new dna
        child = dna()
        # copy parents
        for x in range(0, dna.weights_size):
            child.weights.append(self.weights[x])
        index_to_mutate = random.randint(0, dna.weights_size)
        # randomly pick a percentage to increase or decrease by
        percentage = random.uniform(0.01, 0.25)
        # randomly pick to the mutation factor to be positive or negative
        if(random.random() > 0.5):
            percentage = 1 + percentage
        else:
            percentage = 1 - percentage
        child.weights[index_to_mutate] =  child.weights[index_to_mutate] * percentage
        return child

    def crossover(self, other):
        # do crossover
        child = dna()
        index_to_cross = random.randint(0, dna.weights_size-1)
        for x in range(0,dna.weights_size):
            if x<=index_to_cross:
                child.weights[x]=self.weights[x]
            else:
                child.weights[x]=other.weights[x]
        return child

    def copyNeuron(self):
        copy = neuron()
        copy.weights = self.weights
        return copy

    def evaluate(self):
        neuron = self.copyNeuron()
        self.fitness = neuron.evaluate_neuron()


class neuron:

    def __init__(self):
        self.weights = [random.uniform(-5.0, 5.0), random.uniform(-2.0, 2.0), random.uniform(-5.0, 5.0)]

    def process(self, sensors):
        output = 0
        for x in range(0, dna.weights_size):
            output += sensors[x] * self.weights[x]
        if output < 1.0:
            # jump
            return 1.0
        else:
            # do nothing
            return 0.0

    def evaluate_neuron(self):
        return jumpmain.game_function(self)
