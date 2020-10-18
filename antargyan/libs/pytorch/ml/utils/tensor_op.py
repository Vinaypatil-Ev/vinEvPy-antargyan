import torch


def sort_tensor(X, dim=-1):

    ten, ind = torch.sort(X, dim=dim)

    if X.dim() == 1:
        return ten
    else:
        d1, d2 = X.size()

    if dim == -1:
        return X[torch.arange(d1).unsqueeze(1).repeat((1, d2)), ind]
    elif dim == 0:
        return X[ind, torch.arange(d2)]
    else:
        raise IndexError("wrong dim parameter")
