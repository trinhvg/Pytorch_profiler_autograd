# Pytorch_profiler_autograd
++++++UPDATE+++++++++++++++ \
My server was fixed,  \
A6000 runs well now, no slow problems anymore. \
+++++++++++++++++++++++++++ 

Suppose you already have PyTorch. Then execute the torch_profiler.py file.

More information about torch.autograd.profiler and torch.profiler can found at [(Pytorch_Profiler)](https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html)

## My Pytorch profiler autograd results run on RTX 2080Ti, RTX 3090, and RTX A6000:
(Note I did the Pytorch profiler autograd since my RTX A6000 crashed. I want to test whether it's still fine or not?)

<img src="https://github.com/timmyvg/Pytorch_profiler_autograd/blob/master/image/test_speed.png" width="800" height="700">

## You can also print n most consuming tasks:
ResNet50 "32-bit" training speed
![ResNet50 "32-bit" training speed](https://github.com/timmyvg/Pytorch_profiler_autograd/blob/master/image/ResNet50_speed.png)
