print("Checking which device Torch is using....")
import torch
print("Is CUDA available?", torch.cuda.is_available())
print(torch.cuda.get_device_name(torch.cuda.current_device()))