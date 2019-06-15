#!/usr/bin/env python
# coding: utf-8
from skimage import data
from skimage import io
import matplotlib.pyplot as plt

def example_1():
    image = data.coins()
    print(type(image))
    print(image)
    io.imshow(image)
    io.show()

def example_2():
    image = data.coins()
    methods = [method for method in dir(image) if not method.startswith('_')]
    print(methods)

def example_3():
    image = data.coins()
    print(image.shape)

def example_4():
    image = data.coins()
    print(image.shape[0] * image.shape[1])
    print(image.size)

def example_5():
    image = data.coins()
    print(f'Max: {image.max()}')
    print(f'Min: {image.min()}')
    print(f'Sum: {image.sum()}')

def example_6():
    image = data.coins()
    print(f'Mean: {image.sum() / image.size}')
    print(f'Mean: {image.mean()}')
    print(f'Std: {image.std()}')
    print(f'Var: {image.std() ** 2}')
    print(f'Var: {image.var()}')

def example_7():
    image = data.coins()
    print(image.dtype)
    dtype_uint8 = 2 ** 8
    print(dtype_uint8)
    _min = range(dtype_uint8)[0]
    _max = range(dtype_uint8)[-1]
    print((_min,_max))

def example_8():
    image = data.coins()
    line = 2
    column = 2
    value_img = image[line, column]
    print(value_img)

def example_9():
    image = data.coins()
    line = 2
    column = 2
    print(image[0:line, 0:column])

def example_10():
    image = data.coins()
    line = 2
    column = 2
    crop_img = image[0:line + 1, 0:column + 1].copy()
    print(crop_img)

def example_11():
    image = data.coins()
    line = 2
    column = 2
    crop_img = image[0:line + 1, 0:column + 1].copy()
    print(image[0:line + 1, 0:column+1] == 143, end='\n\n')
    cond_img_0 = crop_img == 143
    print(cond_img_0, end='\n\n')
    print(~cond_img_0)

def example_12():
    image = data.coins()
    line = 2
    column = 2
    crop_img = image[0:line + 1, 0:column + 1].copy()
    cond_img_1 = crop_img != 143
    print(cond_img_1, end='\n\n')
    print(~cond_img_1)

def example_13():
    image = data.coins()
    line = 2
    column = 2
    crop_img = image[0:line + 1, 0:column + 1].copy()
    cond_img_2 = crop_img > 143
    print(cond_img_2, end='\n\n')
    print(~cond_img_2)

def example_14():
    image = data.coins()
    line = 2
    column = 2
    crop_img = image[0:line + 1, 0:column + 1].copy()
    cond_img_3 = crop_img >= 143
    print(cond_img_3, end='\n\n')
    print(~cond_img_3)

def example_15():
    image = data.coins()
    line = 2
    column = 2
    crop_img = image[0:line + 1, 0:column + 1].copy()
    cond_img_4 = crop_img < 143
    print(cond_img_4, end='\n\n')
    print(~cond_img_4)

def example_16():
    image = data.coins()
    line = 2
    column = 2
    crop_img = image[0:line + 1, 0:column + 1].copy()
    cond_img_5 = crop_img <= 143
    print(cond_img_5, end='\n\n')
    print(~cond_img_5)

def example_17():
    image = data.coins()
    line = 3
    column = 3
    crop_img = image[0:line + 1, 0:column + 1].copy()
    print(crop_img, end='\n\n')
    cond_img = crop_img <= 143
    crop_img[cond_img] = 0
    crop_img[~cond_img] = 255
    print(crop_img)

def run_all():
    for n in range(1, 18):
        print(f'------ example_{n:<2} ------')
        eval(f'example_{n}')()

if __name__ == '__main__':
    run_all()
