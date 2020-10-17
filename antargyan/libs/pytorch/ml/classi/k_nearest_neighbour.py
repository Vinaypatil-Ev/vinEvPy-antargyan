import torch
from ..utils import return_torch_tensor
from ..utils import train_test_split

class KNNClassi:
  def __init__(self, X, y, k=3):
    self.k = k
    self.X = return_torch_tensor(X)
    self.y = return_torch_tensor(y)
  
  def _euclidian_distance(self, x_0):
    z = x_0 - self.X
    z = z**2
    z = torch.sum(z, dim=1)
    z = torch.sqrt(z)
    return z

  def predict_(self):
    pass

  def predict(self, X):
    X = return_torch_tensor(X)
    iter = 0
    for x_0 in X:
      distances = self._euclidian_distance(x_0)
      # print(distances[:self.k])
      ten, ind = torch.sort(distances, dim=0)
      # print(ind[:self.k])
      pred = self.y[ind[:self.k]]
      # print(pred.squeeze())
      u,c = torch.unique(pred, dim=0, return_counts=True)
      i = torch.nonzero(c==(c.max())).squeeze(1)
      if len(i) == 2:
        pred_class = torch.index_select(u, 0, i[0])
      else:
        pred_class = torch.index_select(u, 0, i)
      if iter == 0:
        pred_classes = pred_class
        iter = iter + 1
      else:
        pred_classes = torch.cat((pred_classes,pred_class))
    return pred_classes

if __name__ == "__main__":
  x=data[(list(data))[1:-1]]
  y=data[(list(data))[-1:]] 
  x=pd.get_dummies(x)
  # x = x.to_numpy()
  # y = y.to_numpy()
  x.drop(list(x)[-1],axis=1,inplace=True)
  X = torch.tensor(x.to_numpy(), dtype=torch.float64)
  y = torch.tensor(y.to_numpy(), dtype=torch.float64)
  xtrn, xtst, ytrn, ytst = train_test_split(X, y, 0.8)
  print("xtrn, xtst, ytrn, ytst :", xtrn, xtst, ytrn, ytst)
  knn = KNNClassi(xtrn, xtst, k=3)
  pred = knn.predict(ytrn)
  print(pred)
    


