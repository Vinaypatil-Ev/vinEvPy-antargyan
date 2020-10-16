import torch
from antargyan.utils import return_torch_tensor


class LinearRegression:
    """
    from antargyan import LinearRegression
    X=[2,4,5,6,7,8]
    y=[33,44,66,77,99]
    l=LinearRegression(X,y)
    l.fit()
    print(l.train_predictions())
    l.predict([X[1]])
    """
    def __init__(self, x, y, dtype=torch.float32):
        self.dtype = dtype
        self.x = return_torch_tensor(x, self.dtype)
        self.y = return_torch_tensor(y, self.dtype)

    def cal_x(self, X):
        ones = torch.ones(X.size(0)).view(-1,1)
        x = torch.cat((ones, X), dim=1)
        return x

    def cal_theta(self):
        X = self.cal_x(self.x)
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
        x = return_torch_tensor(x, self.dtype)
        X = self.cal_x(x)
        prediction = X.mm(self.theta)
        return prediction


if __name__ == "__main__":
    X=[2,4,5,6,7]
    y=[33,44,66,77,99]
    l=LinearRegression(X,y)
    l.fit()
    print(l.train_predictions())
    print(l.predict([X[1]]))
    print("error:", l.y - l.train_predictions())