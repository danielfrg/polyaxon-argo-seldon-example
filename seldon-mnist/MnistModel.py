import torch
from network import Network
from torchvision import datasets, transforms

class MnistModel(object):
    
    def __init__(self):
        self.model = Network()
        self.model.load_state_dict(torch.load("./model.dat"))

    def predict(self, X, feature_names):
        tensor = torch.from_numpy(X).view(-1, 28, 28)
        t = transforms.Normalize((0.1307,), (0.3081,))
        tensor_norm = t(tensor)
        tensor_norm = tensor_norm.unsqueeze(0)
        out = self.model(tensor_norm.float())
        predictions = torch.nn.functional.softmax(out)
        print(predictions)
        return predictions.detach().numpy()
