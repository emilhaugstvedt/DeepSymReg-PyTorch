import torch

class BaseFunction:

    def __init__(self) -> None:
        self.n_input = 1

class Squared(BaseFunction):

    def torch(self, x):
        return torch.square(x)

class Sin(BaseFunction):

    def torch(self, x):
        return torch.sin(x)

class Cos(BaseFunction):

    def torch(self, x):
        return torch.cos(x)


class Basefunction2:

    def __init__(self) -> None:
        self.n_inputs = 2

class Add(Basefunction2):

    def torch(self, x, y):
        return torch.add(x, y)

class Multiply(Basefunction2):

    def torch(self, x, y):
        return torch.multiply(x, y)
        
    
base_functions = [  Squared.torch, 
                    Sin.torch,
                    Cos.torch,
                    Add.torch,
                    Multiply.torch ]