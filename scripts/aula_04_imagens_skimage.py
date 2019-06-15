#!/usr/bin/env python
# coding: utf-8
from skimage import data
import matplotlib.pyplot as plt

def example_1():
    data_img = [d for d in dir(data) if not d.startswith('_')]

    removes = ['data_dir','expected_warnings',
               'img_as_bool', 'imread',
               'load','osp',
               'use_plugin', 'warn', 'lfw_subset',
               'lbpcascade_frontalface_opencv',
               'lbp_frontal_face_cascade_filename']

    for err in removes:
        if err in data_img:
            data_img.remove(err)

    print(len(data_img))

    for name in data_img:
        caller = getattr(data, name)
        image = caller()

        if isinstance(image, tuple):
            image = image[0]

        plt.figure()
        plt.title(name)
        if image.ndim == 2:
            plt.imshow(image, cmap=plt.cm.gray)
        else:
            plt.imshow(image)
    plt.show()

def example_2():
    data_img = [d for d in dir(data) if not d.startswith('_')]

    removes = ['data_dir','expected_warnings',
               'img_as_bool', 'imread',
               'load','osp',
               'use_plugin', 'warn', 'lfw_subset',
               'lbpcascade_frontalface_opencv',
               'lbp_frontal_face_cascade_filename']

    for err in removes:
        if err in data_img:
            data_img.remove(err)

    print(len(data_img))

    for name in data_img:
        caller = getattr(data, name)
        image = caller()

        if isinstance(image, tuple):
            image = image[0]

        plt.figure()
        plt.title(name)
        if image.ndim == 2:
            plt.imshow(image, cmap=plt.cm.gray)
            plt.show()
        else:
            plt.imshow(image)
            plt.show()

def example_4():
    fig, axes = plt.subplots(4, 5, figsize=(10, 5))
    ax = axes.ravel()
    images = data.lfw_subset()
    for i in range(20):
        ax[i].imshow(images[90+i], cmap=plt.cm.gray)
        ax[i].axis('off')
    fig.tight_layout()
    plt.show()

if __name__ == '__main__':
    example_1()
    example_2()
    example_3()
