import math
import random

def simulatedAnnealing(problem, schedule):
    current = problem.state
    T = schedule(1)
    t = 1
    while T > 0:
        T = schedule(t)
        if problem.value(current) == 0:
            return current
        next = problem.randomNearNeighbour()
        dif = problem.value(next[0]) - problem.value(current)
        print(problem.value(current))
        print(current)
        if dif > 0:
            current = next[0]
        else:
            prob = random.uniform(0, 1)
            if prob < math.exp(dif/T):
                current = next[0]
        t += 0.1