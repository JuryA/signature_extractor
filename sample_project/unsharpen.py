#!/usr/bin/python
"""Soften an image."""
# -*- coding: utf-8 -*-
# -----------------------------------------
# author      : Ahmet Ozlu
# mail        : ahmetozlu93@gmail.com
# date        : 05.05.2019
# -----------------------------------------

import cv2


def unsharpen_mask(image):
    """Soften an input image.

    Parameters
    ----------
    image : numpy ndarray
        The input image.

    Returns
    -------
    numpy ndarray
        The soften image.

    """
    # perform GaussianBlur filter to use it in unsharpening mask
    gaussian_3 = cv2.GaussianBlur(image, (9, 9), 10.0)
    # return unsharpened image
    return cv2.addWeighted(image, 1.5, gaussian_3, -0.5, 0, image)
