from __future__ import print_function
import torch
###########################################
# Tensores são similiares aos Numpy's ndarrays. A diferença é que eles podem ser
# processados pela GPU, melhorando o tempo de processamento
##########################################

###########################################
# Construção de uma matriz 5x3 não inicializada.
##########################################
x = torch.empty(5,3)
print(x)

###########################################
# Construindo uma matriz 5x3  inicializada com valores randomicos
##########################################
x = torch.rand(5,3)
print(x)

x = torch.zeros(5,3, dtype=torch.long)
print(x)

x = torch.tensor([5.5,3])
print(x)
