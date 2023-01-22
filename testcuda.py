import torch
import torchvision
print(torch.__version__)
print(torch.version.cuda)
print(torch.cuda.is_available() ) ## 输出应该是True

print(torchvision.__version__)
print(torchvision.version.cuda)