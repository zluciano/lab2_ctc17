import random

class queen():
    def __init__(self, N):
        self.N = N
        self.state = []
        for i in range(0, self.N):
            self.state.append(i)
        random.shuffle(self.state)

    def value(self, state):
        value = 0
        for i in range(0, self.N):
            for j in range(i+1, self.N):
                if i-state[i] == j-state[j] or i+state[i] == j+state[j]:
                    value += 1
        return -value

    def randomNearNeighbour(self, state):
        curr = random.randint(0, self.N-1)
        new = random.randint(0, self.N-1)
        nstate = state.copy()
        while new == state[curr]:
            new = random.randint(0, self.N-1)
        for i in range(0, self.N):
            if state[i] == new:
                nstate[i] = state[curr]
        nstate[curr] = new
        return nstate
    
    """ def randomNearNeighbour(self, state):
        neig = []
        nstate = state.copy()
        for k in range(1, self.N):
            for i in range(0, self.N):
                nstate[i] = (state[i]-k)%self.N
                for j in range(0, self.N):
                    if state[j] == (state[i]-k)%self.N:
                        nstate[j] = (state[j]+k)%self.N
                neig.append(nstate)
                nstate = state.copy()
            
        return random.sample(neig, 1) """