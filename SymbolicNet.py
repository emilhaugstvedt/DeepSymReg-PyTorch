import torch
import torch.nn as nn
import torch.optim as optim
import math
from tqdm import tqdm


class SymbolicLayer(nn.Module):
    def __init__(self, input_size, output_size, functions) -> None:
        super().__init__()
        self.functions = functions
        self.n_functions = len(functions)

        self.single_input_functions = [f for f in self.functions if f.n_inputs == 1]
        self.n_single = len(self.single_input_functions)

        self.double_input_functions = [f for f in self.functions if f.n_inputs == 2]
        self.n_double = len(self.double_input_functions)

        self.n_inputs_func = self.n_single + 2 * self.n_double

        weights = torch.Tensor(input_size, self.n_inputs_func)
        self.weights = nn.Parameter(weights)
        nn.init.kaiming_uniform_(self.weights, a=math.sqrt(5))

        self.output = None

    def forward(self, x):

        self.output = []

        x = torch.matmul(x, self.weights)

        i_out = i_in = 0

        while i_out < self.n_single:
            self.output.append(self.single_input_functions[i_out].torch(x[i_in]))
            i_out += 1
            i_in += 1

        while i_out < self.n_functions:
            self.output.append(self.double_input_functions[i_out - self.n_single].torch(x[i_in], x[i_in + 1]))
            i_out += 1
            i_in += 2
        
        return torch.stack(self.output)

    def get_weights(self):
        return self.weights

class SymbolicNet(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size, functions: list):
        super().__init__()
        self.input_size = input_size
        self.output_size = output_size
        self.functions = functions
        self.n_funcs = len(functions)
        self.fc1 = SymbolicLayer(input_size, hidden_size, functions=functions)
        #self.fc2 = SymbolicLayer(hidden_size, hidden_size, functions=functions)
        #self.output = nn.Linear(hidden_size, output_size)
        #for param in self.output.parameters():
        #    nn.init.ones_(param)
        #    param.requires_grad = False

    def forward(self, x):
        x = self.fc1(x)
        #x = self.fc2(x)
        #x = self.output(x)
        x = torch.sum(x)
        return x
    
    def train_n_epochs(self, x, y, epochs=100, lr=0.0001):
        optimizer = optim.Adam(self.parameters(), lr=lr)
        loss_fn = nn.MSELoss()
        for epoch in range(epochs):
            total_loss = 0 # Storing total loss during training
            # Forward pass and weight update for each sample
            for i in tqdm(range(len(x))):
                optimizer.zero_grad()
                output = self.forward(x[i])
                loss = loss_fn(output, y[i])
                loss.backward()
                optimizer.step()
                total_loss += loss.item()
        
            if epoch % 100 == 0:
                print(f'Epoch: {epoch} Loss: {loss.item()}')
    
    def get_weights(self):
        return self.fc1.get_weights() #self.output.weight