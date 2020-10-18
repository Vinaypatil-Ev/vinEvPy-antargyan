import torch


def train_test_split(x, y, trn_size, shuffle=False):
    if not isinstance(x, torch.tensor) and not isinstance(y, torch.tensor):
        raise TypeError("x, y must be torch Tensor")

    if len(x) != len(y):
        raise ValueError("x and y dont have same length")

    if shuffle is True:
        x = x[torch.randperm(x.size()[0])]
        y = y[torch.randperm(y.size()[0])]

    if isinstance(trn_size, (int)) and trn_size < len(x):
        x1, x2 = torch.split(x, trn_size)
        y1, y2 = torch.split(y, trn_size)
        return x1, x2, y1, y2
    elif isinstance(trn_size, float):
        size = int(trn_size * len(x))
        size = [size, len(x) - size]
        x1, x2 = torch.split(x, size)
        y1, y2 = torch.split(y, size)
        return x1, x2, y1, y2
    else:
        raise TypeError("trn_size should int or float")
