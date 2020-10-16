from ..utils.data_format import return_torch_tensor

class KNN:
  def __init__(self, X, y, k=1):
    self.k = k
    self.X = return_torch_tensor(X)
    self.y = return_torch_tensor(y)
  
  def _euclidian_distance(self, x_0):
    z = x_0 - self.X
    z = z**2
    z = torch.sum(z, dim=1)
    z = torch.sqrt(z)
    return z

  def _sort_tensor(self, X, dim=-1):
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
  
  def predict_(self):
    pass

  def predict(self, X):
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
    


