import os, sys; sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from dezero.datasets import MNIST
from dezero.data import DataLoader

batch_size = 10
max_epoch = 1

train_set = MNIST(train=True)
test_set = MNIST(train=False)
train_loader = DataLoader(train_set, batch_size)
test_loader = DataLoader(test_set, batch_size, shuffle=False)

for epoch in range(max_epoch):
    for x, t in train_loader:
        print(x.shape, t.shape)
        break

    for x, t in test_loader:
        print(x.shape, t.shape)
        break