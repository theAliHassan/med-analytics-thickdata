# transforms_utils.py

import torch

class ToThreeChannels:
    """
    Convert grayscale 1×HxW tensor into 3×HxW by repeating the channel.
    Safe to use with multiprocessing DataLoader workers.
    """
    def __call__(self, x):
        return x.repeat(3, 1, 1)
