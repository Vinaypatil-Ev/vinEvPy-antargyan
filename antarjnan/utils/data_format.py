import torch
import tensorflow as tf
import numpy as np

def is_torch_tensor(x):
    return torch.is_tensor(x)
def is_tf_tensor(x):
    return tf.is_tensor(x)
def is_nparray(x):
    return isinstance(x,np.ndarray)

def tf_to_torch(x):
    pass

def torch_to_tf(x):
    pass
    
def return_torch_tensor(ten):
    if is_torch_tensor(ten):
        return ten
    elif is_tf_tensor(ten):
        return tf_to_torch(ten)
    else is_nparray(ten):
        return torch.from_numpy(ten)
    