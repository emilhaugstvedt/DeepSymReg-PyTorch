import torch
from torch.utils.data import Dataset

class Dataset_duffing(Dataset):

    def __init__(self, data,delta_time):
        self.timesteps = 1
        self.DT = delta_time

        self.x, self.x_mean, self.x_std = self.organize_features(data)

        self.y, self.y_mean, self.y_std, self.y_non_norm = self.organize_target(data)

        self.x_non_norm = torch.flatten(data,start_dim=0, end_dim=1)

        self.n_samples = self.x.shape[0]



    def __getitem__(self,index):

        X = self.x[index]

        Y = self.y[index]

        return X, Y

    def __len__(self):
        return self.n_samples

    def organize_features(self, data):
        #standard normalize input: (x-mean)/std(x)
        temp = torch.flatten(data, start_dim=0, end_dim=1)
        mean = torch.mean(temp, axis=0)
        std = torch.std(temp, axis=0)

        t_steps = data.shape[1]
        no_sim = data.shape[0]

        temp_input = torch.empty(no_sim, t_steps-1, data.shape[2])

        for i in range(data.shape[0]):
            temp_input[i,:,:] = (data[i,0:t_steps-1,:] - mean)/std

        x = torch.flatten(temp_input, start_dim=0, end_dim = 1)

        return x, mean, std


    def organize_target(self, data):
        #Standard normalize output: (y- mean(y))/std(y)

        t_steps = data.shape[1]
        no_sim = data.shape[0]

        temp_target = torch.empty(data.shape[0], data.shape[1] - 1, 2)

        for i in range(no_sim):
            for j in range(t_steps - 1):
                temp_target[i, j, :] = (data[i, j + 1, 0:2] - data[i, j, 0:2]) / self.DT

        y_not_norm = torch.flatten(temp_target, start_dim=0, end_dim=1)

        mean = torch.mean(y_not_norm, axis=0)
        std = torch.std(y_not_norm, axis=0)
        y = (y_not_norm - mean)/std

        return y, mean, std, y_not_norm