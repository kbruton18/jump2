import random
import jumpmain

class dna:
    weights_size = 3

    def __init__(self):
        self.weights=[]
        for c in range(0, dna.weights_size):
            #randomly assign weights in range -5.0 to 5.0
            self.weights.append(random.uniform(-3.0, 3.0))

    def mutate(self):
        # create a new dna
        child = dna()
        # copy paren'ts 
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
        for x in range(0, dna.weights_size):
            if random.random() > 0.5:
                child.weights[x] = self.weights[x]
            else:
                child.weights[x] = other.weights[x]
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
        self.weights = [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]


    def process(self, sensors):
        output = 0
        for x in range(0, dna.weights_size):
            output += sensors[x] * self.weights[x]
        if output > 0:
            #print 'jump'
            return 1.0
        else:
            #print 'not do anything'
            return 0.0

    def evaluate_neuron(self):
        return jumpmain.game_function(self)

