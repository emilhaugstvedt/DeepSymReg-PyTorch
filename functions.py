from random import expovariate
import torch
import sympy as sym

class BaseFunction:

    def __init__(self) -> None:
        self.n_inputs = 1

class Constant(BaseFunction):

    def __init__(self) -> None:
        super().__init__()

    def torch(self, x):
        return torch.ones(x.shape)

    def sym(self):
        return "1"

class Square(BaseFunction):

    def __init__(self) -> None:
        super().__init__()

    def torch(self, x):
        return torch.square(x)

    def sym(self, x):
        return x ** 2
    
    def as_string(self):
        return "Square"

class Sin(BaseFunction):

    def __init__(self) -> None:
        super().__init__()

    def torch(self, x):
        return torch.sin(x)

    def sym(self, x):
        return sym.sin(x)
    
    def as_string(self):
        return "Sin"

class Cos(BaseFunction):

    def __init__(self) -> None:
        super().__init__()

    def torch(self, x):
        return torch.cos(x)
        
    def sym(self, x):
        return sym.cos(x)
    
    def as_string(self):
        return "Cos"

class Linear(BaseFunction):

    def __init__(self) -> None:
        super().__init__()

    def torch(self, x):
        return x
    
    def sym(sel, x):
        return x
    
    def as_string(self):
        return "Linear"

class Sqrt(BaseFunction):

    def __init__(self) -> None:
        super().__init__()

    def torch(self, x):
        return torch.sqrt(x)

    def sym(self):
        return sym.sqrt(x)

class Exp(BaseFunction):
    
    def __init__(self) -> None:
        super().__init__()
    
    def torch(self, x):
        return torch.exp(x)
    
    def sym(self, x):
        return sym.exp(x)
        
    def as_string(self):
        return "Exp"

class Pow(BaseFunction):

    def __init__(self, exponent) -> None:
        super().__init__()
        self.exponent = exponent
    
    def torch(self, x):
        return torch.pow(x, self.exponent)
    
    def sym(self, x):
        return x ** self.exponent
    
    def as_string(self):
        return f"Pow({self.exponent})"
    


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

    def sym(self, x, y):
        return x * y
    
    def as_string(self):
        return "Multiply"
        
    
base_functions = [Square(), Linear(), Sin(), Cos()]