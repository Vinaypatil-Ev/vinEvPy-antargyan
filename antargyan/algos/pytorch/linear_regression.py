import torch
from antargyan.utils import return_torch_tensor


class LinearRegression:
    def __init__(self, x, y,dtype=torch.float32):
        self.dtype=dtype
        self.x = return_torch_tensor(x, self.dtype)
        self.y = return_torch_tensor(y, self.dtype)

    def cal_x(self, X):
        ones = torch.ones(self.x.size(0))
        x = torch.cat((ones, X), axis=1)
        return x

    def cal_theta(self):
        X = self.cal_X(self.x)
        theta = torch.inverse(X.t().mm(X))
        theta = theta.mm(X.t())
        theta = theta.mm(self.y)
        return theta

    def fit(self):
        self.X = self.cal_x(self.x)
        self.theta = self.cal_theta()

    def train_predictions(self):
        pred = self.X.mm(self.theta)
        return pred

    def predict(self, x):
        x = self.return_torch_tensor(x, self.dtype)
        X = self.cal_x(x)
        prediction = X.mm(self.theta)
        return prediction
