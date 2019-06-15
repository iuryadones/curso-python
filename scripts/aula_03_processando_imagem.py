#!/usr/bin/env python
# coding: utf-8
from skimage import data
from skimage import io
from skimage import filters
from skimage import morphology


io.cmap = 'gray'

def example_1():
    image = data.coins()
    io.imshow(image)
    io.show()

def example_2():
    methods = [fil for fil in dir(filters) if not fil.startswith('_')]
    print(methods)

def example_3():
    image = data.coins()
    filtered = filters.gaussian(image)
    io.imshow(filtered)
    io.show()

def example_3():
    image = data.coins()
    filtered = filters.roberts(image)
    io.imshow(filtered)
    io.show()

def example_4():
    methods = [mor for mor in dir(morphology) if not mor.startswith('_')]
    print(methods)

def example_5():
    image = data.coins()
    selem = morphology.square(width=2)
    print(selem)
    median_selem = filters.median(image, selem)
    io.imshow(median_selem)
    io.show()

def example_6():
    image = data.coins()
    selem = morphology.disk(radius=2)
    print(selem)
    median_selem = filters.median(image, selem)
    io.imshow(median_selem)
    io.show()

def example_7():
    image = data.coins()
    selem = morphology.octagon(2,2)
    print(selem)
    median_selem = filters.median(image, selem)
    io.imshow(median_selem)
    io.show()

def example_8():
    image = data.coins()
    feature = filters.gaussian(image, sigma=1)
    feature = filters.median(feature, morphology.disk(3))
    feature = filters.median(feature, morphology.disk(5))
    cond = feature < feature.max() / 2
    feature[cond] = 0
    feature[~cond] = 1
    io.imshow(feature, cmap='gray')
    io.show()

    feature = filters.gaussian(feature,sigma=1)
    feature = filters.roberts(feature)
    io.imshow(feature, cmap='gray')
    io.show()


def run_all():
    for n in range(1, 9):
        print(f'------ example_{n:<2} ------')
        eval(f'example_{n}')()

if __name__ == '__main__':
    run_all()
