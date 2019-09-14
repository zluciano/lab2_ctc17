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
    
    def randomNearNeighbour(self):
        neig = []
        state = self.state.copy()
        for k in range(1, self.N):
            for i in range(0, self.N):
                state[i] = (state[i]-k)%self.N
                for j in range(0, self.N):
                    if self.state[j] == (self.state[i]-k)%self.N:
                        state[j] = (state[j]+k)%self.N
                neig.append(state)
                state = self.state.copy()
            
        return random.sample(neig, 1)