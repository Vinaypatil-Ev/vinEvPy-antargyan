import torch
from antargyan.util.tensor import return_torch_tensor

class LinearRegreesion:
    def __init__(x,y):
        self.x=return_torch_tensor(x)
        self.y=return_torch_tensor(y)
        
    def cal_x(self):
        ones=torch.ones(self.x.size(0))
        x=torch.cat((ones,self.x),axis=1)
        return x
    
    def cal_theta(self):
        X=self.cal_X(self.x)
        theta=torch.inverse(X.t().mm(X))
        theta=theta.mm(X.t())
        theta=theta.mm(self.y)
        return theta
    
    def fit(self):
        self.X=self.cal_X(self.x)
        self.theta=self.cal_theta()
    
    def predict(self,x):
        x=self.return_torch_tensor(x,self.dtype)
        X=self.cal_X(x)
        prediction=X.mm(self.theta)
        return prediction