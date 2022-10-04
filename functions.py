import torch
import sympy

class BaseFunction:

    def __init__(self) -> None:
        self.n_inputs = 1

class Square(BaseFunction):

    def __init__(self) -> None:
        super().__init__()

    def torch(self, x):
        return torch.square(x)

    def sympy(self):
        return sympy.powdenest("x**2")

class Sin(BaseFunction):

    def __init__(self) -> None:
        super().__init__()

    def torch(self, x):
        return torch.sin(x)

    def sympy(self):
        return sympy.sin("x")

class Cos(BaseFunction):

    def __init__(self) -> None:
        super().__init__()

    def torch(self, x):
        return torch.cos(x)
        
    def sympy(self, x):
        return sympy.cos(x)

class Linear(BaseFunction):

    def __init__(self) -> None:
        super().__init__()

    def torch(self, x):
        return x


class Basefunction2:

    def __init__(self) -> None:
        self.n_inputs = 2

class Add(Basefunction2):

    def __init__(self) -> None:
        super().__init__()

    def torch(self, x, y):
        return torch.add(x, y)

class Multiply(Basefunction2):

    def __init__(self) -> None:
        super().__init__()

    def torch(self, x, y):
        return torch.multiply(x, y)
        
    
base_functions = [Square(), Sin()]