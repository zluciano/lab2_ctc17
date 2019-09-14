from nQueens import queen
from simulatedAnnealing import simulatedAnnealing
import math

def func(i):
    return 1/(1+i)

problem = queen(4)
schedule = func

solution = simulatedAnnealing(problem, schedule)

print(solution)