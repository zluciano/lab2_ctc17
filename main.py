from nQueens import queen
from simulatedAnnealing import simulatedAnnealing
import math

def func(i):
    return 1/(1+i)

problem = queen(50)
schedule = func

solution = simulatedAnnealing(problem, schedule)

for i in range(problem.N):
    for j in range(problem.N):
        if j != solution[i]:
            print(". ", end="")
        else:
            print("Q ", end="")
    print("")