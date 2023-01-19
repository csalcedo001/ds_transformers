import numpy as np

# OP_PUSH = 0
# OP_POP = 1
# TOKEN_0 = 2
# TOKEN_1 = 3
# TOKEN_ERR = 4

# OP_PUSH = np.array([1, 0, 0, 0, 0])
# OP_POP  = np.array([0, 1, 0, 0, 0])
# TOKEN_0 = np.array([0, 0, 1, 0, 0])
# TOKEN_1 = np.array([0, 0, 0, 1, 0])
# TOKEN_ERR = np.array([0, 0, 0, 0, 1])

OP_PUSH = "OP_PUSH"
OP_POP  = "OP_POP"
TOKEN_0 = "1"
TOKEN_1 = "0"
TOKEN_ERR = "ERR"
    


class DataGenerator():
    def __init__(
            self,
            push_prob=0.5,
            min_seq_len=1,
            is_error_free=True,
        ):

        self.push_prob = push_prob
        self.min_seq_len = min_seq_len
        self.is_error_free = is_error_free
        
        self.reset()
    
    def reset(self):
        self.stack = []
        self.input = []
        self.output = []

    def sample(self):
        while len(self.input) < self.min_seq_len:
            if self.is_error_free and len(self.stack) == 0:
                self._push()
            else:
                self._random_op()
        
        while len(self.stack) > 0:
            self._random_op()
        
        return self.input, self.output
    
    def _push(self):
        value = TOKEN_0 if np.random.uniform() < 0.5 else TOKEN_1

        self.stack.append(value)

        self.input.append(OP_PUSH)
        self.input.append(value)
    
    def _pop(self):
        value = self.stack.pop() if len(self.stack) > 0 else TOKEN_ERR

        self.input.append(OP_POP)
        self.output.append(value)
    
    def _random_op(self):
        if np.random.uniform() < self.push_prob:
            self._push()
        else:
            self._pop()