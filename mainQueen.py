from nQueens import queen
from simulatedAnnealing import simulatedAnnealing
import math

def func(i):
    return 1/(1+i)


# Solução para um valor de N de livre escolha, altere abaixo:
N = 25

problem = queen(N)
schedule = func

solution = simulatedAnnealing(problem, schedule)

print(solution)

for i in range(problem.N):
    for j in range(problem.N):
        if j != solution[i]:
            print(". ", end="")
        else:
            print("Q ", end="")
    print("")
