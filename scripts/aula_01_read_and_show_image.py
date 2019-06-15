#!/usr/bin/env python
# coding: utf-8
import matplotlib.pyplot as plt
from skimage import data
from skimage import io
from skimage.filters import sobel


def example_1():
    image = data.coins()
    print(type(image))
    print(image)
    io.imshow(image)
    io.show()

def example_2():
    image = data.coins()
    edges = sobel(image)
    print(type(edges))
    print(edges)
    io.imshow(edges)
    io.show()

if __name__ == '__main__':
    example_1()
    example_2()
