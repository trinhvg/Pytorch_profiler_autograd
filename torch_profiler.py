import torch
import torchvision.models as models
import os
import torch.nn.functional as F
import torch.optim as optim

os.environ['CUDA_VISIBLE_DEVICES'] = '3'


def profiler_model(net_name):
    net = eval(f'models.{net_name}().cuda()')

    bach_size = 16
    imgs = torch.randn(bach_size, 3, 512, 512).cuda()
    true = torch.randint(0, 4, (bach_size,)).cuda()

    optimizer = optim.Adam(net.parameters(), lr=0.001)
    net = net.train()
    with torch.autograd.profiler.profile(use_cuda=True) as prof:
        net.zero_grad()  # not rnn so not accumulate
        for epoch in range(5):   # train 5 epoch
            logit = net(imgs)

            loss = F.cross_entropy(logit, true, reduction='mean')
            loss.backward()
            optimizer.step()
        # -----------------------------------------------------------
    # print ten most consuming time  operations
    return print(prof.key_averages().table(sort_by="cuda_time_total", row_limit=10))


net_list = ['resnet50', 'alexnet', 'vgg16', 'squeezenet1_0', 'shufflenet_v2_x1_0', 'resnext50_32x4d',
            'mobilenet_v2', 'mnasnet1_0', 'densenet121', 'efficientnet_b0']

for net_name in net_list:
    print('Network: ', net_name)
    profiler_model(net_name)
