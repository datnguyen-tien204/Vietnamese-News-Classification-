import numpy as np
import torch
from torch.utils.data import Dataset


class TextDataset(Dataset):
    def __init__(self, X, Y):
        self.X = X
        self.y = Y

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        x = self.X[idx][0].astype(np.float32)
        y = self.y[idx]
        return torch.from_numpy(x), y

    import numpy as np
    # import torch
    # from torch.utils.data import Dataset
    #
    # # Kiểm tra xem có GPU hỗ trợ CUDA hay không
    # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    #
    # class TextDataset(Dataset):
    #     def __init__(self, X, Y):
    #         self.X = X
    #         self.y = Y.to(device)  # Chuyển dữ liệu sang CUDA
    #
    #     def __len__(self):
    #         return len(self.y)
    #
    #     def __getitem__(self, idx):
    #         x = self.X[idx][0].astype(np.float32)
    #         y = self.y[idx]
    #         return torch.from_numpy(x).to(device), y  # Chuyển dữ liệu sang CUDA

