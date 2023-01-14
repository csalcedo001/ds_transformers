import numpy as np

# OP_PUSH = 0
# OP_POP = 1
# TOKEN_0 = 2
# TOKEN_1 = 3
# TOKEN_ERR = 4

OP_PUSH = np.array([1, 0, 0, 0, 0])
OP_POP  = np.array([0, 1, 0, 0, 0])
TOKEN_0 = np.array([0, 0, 1, 0, 0])
TOKEN_1 = np.array([0, 0, 0, 1, 0])
TOKEN_ERR = np.array([0, 0, 0, 0, 1])
    


class DataGenerator():
    def __init__(self, push_prob=0.5):
        self.push_prob = push_prob

        self.stack = []
        self.input = []
        self.output = []

    def sample(self):
        self._push()

        while len(self.stack) > 0:
            self._random_op()
        
        return self.input, self.output
    
    def _push(self):
        value = TOKEN_0 if np.random.uniform() < 0.5 else TOKEN_1

        self.stack.append(value)

        self.input.append(OP_PUSH)
        self.input.append(value)
    
    def _pop(self):
        value = self.stack.pop()

        self.input.append(OP_POP)
        self.output.append(value)
    
    def _random_op(self):
        if np.random.uniform() < self.push_prob:
            self._push()
        else:
            self._pop()