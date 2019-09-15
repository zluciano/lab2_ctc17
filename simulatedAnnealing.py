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
        next = problem.randomNearNeighbour(current)
        dif = problem.value(next) - problem.value(current)
        if dif > 0:
            current = next
        else:
            prob = random.uniform(0, 1)
            if prob < math.exp(dif/T):
                current = next
        t += 1