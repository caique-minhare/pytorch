from __future__ import print_function
import torch

y = torch.rand(5,3)
x = torch.rand(5,3)
print(x+y)

result = torch.empty(5,3)
torch.add(x,y, out=result)
print(result)

y.add_(x)
print(y)


x = torch.randn(4,4)
y = x.view(16)
z = x.view(-1,8)
print(x.size(), y.size(), z.size())

x = torch.randn(1)
print(x)
print(x.item())
