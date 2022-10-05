import torch
import sympy

class BaseFunction:

    def __init__(self) -> None:
        self.n_inputs = 1

class Constant(BaseFunction):

    def __init__(self) -> None:
        super().__init__()

    def torch(self, x):
        return torch.ones(x.shape)

    def sympy(self):
        return "1"

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
        
    def sympy(self):
        return sympy.cos("x")

class Linear(BaseFunction):

    def __init__(self) -> None:
        super().__init__()

    def torch(self, x):
        return 1 * x
    
    def sympy(self):
        return "x"

class Sqrt(BaseFunction):

    def __init__(self) -> None:
        super().__init__()

    def torch(self, x):
        return torch.sqrt(x)

    def sympy(self):
        x = sympy.Symbol('x')
        return sympy.sqrt(x)

class Exp(BaseFunction):
    
        def __init__(self) -> None:
            super().__init__()
    
        def torch(self, x):
            return torch.exp(x)
    
        def sympy(self):
            x = sympy.Symbol('x')
            return sympy.exp(x)


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
        
    
base_functions = [Square(), Linear(), Sin(), Cos()]