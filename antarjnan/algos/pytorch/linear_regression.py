import torch
from antarjnan.util import tesor

class LinearRegreesion:
    def __init__(x,y):
        self.x=tensor.return_torch_tensor(x)
        self.y=tensor.return_torch_tensor(y)
        
    def cal_x:
        ones=torch.ones(self.x.size(0))
        x=torch.cat((ones,self.x),axis=1)
        return x