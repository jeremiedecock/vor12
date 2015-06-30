#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2015 Jérémie DECOCK (http://www.jdhp.org)

"""
OpenCV - Extract one color.

Required: opencv library (Debian: aptitude install python-opencv)

See: https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html#hough-circles
     https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#object-tracking
     Oreilly's book "Learning OpenCV" (first edition) p.158 for details about Hough transforms.

     http://txt.arboreus.com/2014/10/21/remove-circles-from-an-image-in-python.html
     http://wiki.elphel.com/index.php?title=OpenCV_Tennis_balls_recognizing_tutorial
     http://stackoverflow.com/questions/28521783/python-opencv-houghcircles-not-giving-good-results
     http://computer-vision-talks.com/articles/how-to-detect-circles-in-noisy-image/
     http://www.pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/
"""

# TODO:
# - [ ] Améliorer la gestion multithread Tkinter + OpenCV (sortie, ...)
# - [ ] Ajouter un Label à côté des scales Tkinter
# - [ ] Afficher dans une fenetre à part les couleurs "frame_lower_color" et "frame_upper_color"
# - [ ] Afficher le canny edge detector utilisé en interne par Hough Circle Transform

from __future__ import print_function

import cv2 as cv
import numpy as np
import argparse
import Tkinter as tk
import threading

DEFAULT_LOWER_COLOR_H = 105   # 110   # 105
DEFAULT_LOWER_COLOR_S = 135   # 50    # 135
DEFAULT_LOWER_COLOR_V = 68    # 50    # 68
                            
DEFAULT_UPPER_COLOR_H = 120   # 130   # 120
DEFAULT_UPPER_COLOR_S = 220   # 255   # 220
DEFAULT_UPPER_COLOR_V = 180   # 255   # 180

DEFAULT_HCT_ACCUMULATOR_RESOLUTION = 1.2
DEFAULT_HCT_CANNY_EDGE_THRESHOLD = 50
DEFAULT_HCT_ACCUMULATOR_THRESHOLD = 10  # 30  # 10
DEFAULT_HCT_MIN_RADIUS = 0
DEFAULT_HCT_MAX_RADIUS = 0

def main():

    # Parse the programm options (get the path of the image file to read) #####

    parser = argparse.ArgumentParser(description='An opencv snippet.')
    parser.add_argument("--cameraid", "-i",  help="The camera ID number (default: 0)", type=int, default=0, metavar="INTEGER")
    args = parser.parse_args()

    device_number = args.cameraid

    # TkInter #################################################################

    root = tk.Tk()

    root.geometry("500x600")   # Set the size of the "root" window

    frame_lower_color = tk.LabelFrame(root, text="Lower color", padx=2, pady=2)
    frame_upper_color = tk.LabelFrame(root, text="Upper color", padx=2, pady=2)
    frame_hct = tk.LabelFrame(root, text="Hough Circle Transform", padx=2, pady=2)

    frame_lower_color.pack(fill=tk.X, expand=1, padx=5, pady=3)
    frame_upper_color.pack(fill=tk.X, expand=1, padx=5, pady=3)
    frame_hct.pack(fill=tk.X, expand=1, padx=5, pady=3)

    # See: http://effbot.org/tkinterbook/scale.htm
    scale_lower_color_H = tk.Scale(frame_lower_color, from_=0, to=255, orient=tk.HORIZONTAL)
    scale_lower_color_S = tk.Scale(frame_lower_color, from_=0, to=255, orient=tk.HORIZONTAL)
    scale_lower_color_V = tk.Scale(frame_lower_color, from_=0, to=255, orient=tk.HORIZONTAL)

    scale_upper_color_H = tk.Scale(frame_upper_color, from_=0, to=255, orient=tk.HORIZONTAL)
    scale_upper_color_S = tk.Scale(frame_upper_color, from_=0, to=255, orient=tk.HORIZONTAL)
    scale_upper_color_V = tk.Scale(frame_upper_color, from_=0, to=255, orient=tk.HORIZONTAL)

    scale_hct_accumulator_resolution = tk.Scale(frame_hct, from_=0, to=16, orient=tk.HORIZONTAL)
    scale_hct_canny_edge_threshold = tk.Scale(frame_hct, from_=0, to=255, orient=tk.HORIZONTAL)
    scale_hct_accumulator_threshold = tk.Scale(frame_hct, from_=0, to=255, orient=tk.HORIZONTAL)
    scale_hct_min_radius = tk.Scale(frame_hct, from_=0, to=255, orient=tk.HORIZONTAL)
    scale_hct_max_radius = tk.Scale(frame_hct, from_=0, to=255, orient=tk.HORIZONTAL)

    scale_lower_color_H.set(DEFAULT_LOWER_COLOR_H)
    scale_lower_color_S.set(DEFAULT_LOWER_COLOR_S)
    scale_lower_color_V.set(DEFAULT_LOWER_COLOR_V)

    scale_upper_color_H.set(DEFAULT_UPPER_COLOR_H)
    scale_upper_color_S.set(DEFAULT_UPPER_COLOR_S)
    scale_upper_color_V.set(DEFAULT_UPPER_COLOR_V)

    scale_hct_accumulator_resolution.set(DEFAULT_HCT_ACCUMULATOR_RESOLUTION)
    scale_hct_canny_edge_threshold.set(DEFAULT_HCT_CANNY_EDGE_THRESHOLD)
    scale_hct_accumulator_threshold.set(DEFAULT_HCT_ACCUMULATOR_THRESHOLD)
    scale_hct_min_radius.set(DEFAULT_HCT_MIN_RADIUS)
    scale_hct_max_radius.set(DEFAULT_HCT_MAX_RADIUS)

    scale_lower_color_H.pack(fill=tk.X, expand=1)
    scale_lower_color_S.pack(fill=tk.X, expand=1)
    scale_lower_color_V.pack(fill=tk.X, expand=1)

    scale_upper_color_H.pack(fill=tk.X, expand=1)
    scale_upper_color_S.pack(fill=tk.X, expand=1)
    scale_upper_color_V.pack(fill=tk.X, expand=1)

    scale_hct_accumulator_resolution.pack(fill=tk.X, expand=1)
    scale_hct_canny_edge_threshold.pack(fill=tk.X, expand=1)
    scale_hct_accumulator_threshold.pack(fill=tk.X, expand=1)
    scale_hct_min_radius.pack(fill=tk.X, expand=1)
    scale_hct_max_radius.pack(fill=tk.X, expand=1)

    # OpenCV ##################################################################

# As said in https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html:
#
#   "In HSV, it is easier to represent a color than RGB color-space. In our
#   application, we will try to extract a blue colored object. So here is the
#   method:
#   
#   1. Take each frame of the video
#   2. Convert from BGR to HSV color-space
#   3. We threshold the HSV image for a range of blue color
#   4. Now extract the blue object alone, we can do whatever on that image we want."

# How to find HSV values to track?
#
#   As said in https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html:
#   This is a common question found in stackoverflow.com. It is very simple and
#   you can use the same function, cv2.cvtColor(). Instead of passing an image,
#   you just pass the BGR values you want. For example, to find the HSV value of
#   Green, try following commands in Python terminal:
#
#     >>> green = np.uint8([[[0,255,0 ]]])
#     >>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
#     >>> print hsv_green
#     [[[ 60 255 255]]]
#
#   Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper
#   bound respectively. Apart from this method, you can use any image editing
#   tools like GIMP or any online converters to find these values, but don’t
#   forget to adjust the HSV ranges."

    video_capture = cv.VideoCapture(device_number)

    print("Press q to quit.")

    def opencv_main_loop():
        while(True):
            # Capture frame-by-frame.

            # 'ret' is a boolean ('True' if frame is read correctly, 'False' otherwise).
            # 'img_np' is an numpy array.
            ret, img_bgr = video_capture.read()

            # IMAGE PROCESSING ################################

            img_blur = cv.GaussianBlur(img_bgr, (5,5), 0)

            # Convert BGR color space to HSV
            img_hsv = cv.cvtColor(img_blur, cv.COLOR_BGR2HSV)

            # Define range of blue color in HSV
            lower_color_H = scale_lower_color_H.get()
            lower_color_S = scale_lower_color_S.get()
            lower_color_V = scale_lower_color_V.get()
                        
            upper_color_H = scale_upper_color_H.get()
            upper_color_S = scale_upper_color_S.get()
            upper_color_V = scale_upper_color_V.get()

            lower_color = np.array([lower_color_H, lower_color_S, lower_color_V])
            upper_color = np.array([upper_color_H, upper_color_S, upper_color_V])

            # Threshold the HSV image to get only blue colors
            img_mask = cv.inRange(img_hsv, lower_color, upper_color)

            # Hough Circle Transform
            # See Oreilly's book "Learning OpenCV" (first edition) p.158 for details about Hough transforms.
            # - method : the only method available is CV_HOUGH_GRADIENT so...
            # - dp : the resolution of the accumumator image used (allow to create
            #   an accumulator of a lower resolution than the input image). It must
            #   be greater or equal to 1. A value of "1" keep the original size; a
            #   value of "2" divide the resolution by 2, ...
            # - min_dist : the minimum distance between 2 circles (distances in
            #   pixels). Should be proportional to the image size (img_bgr.shape[0]
            #   and img_bgr.shape[1]).
            # - param1 : the edge (Canny) threshold.
            # - param2 : the accumulator threshold.
            # - minRadius : the minimum radius of circles that can be found (radius
            #   in pixels). Should be proportional to the image size
            #   (img_bgr.shape[0] and img_bgr.shape[1]).
            # - maxRadius : the maximum radius of circles that can be found (radius
            #   in pixels). Should be proportional to the image size
            #   (img_bgr.shape[0] and img_bgr.shape[1]).
            method = cv.cv.CV_HOUGH_GRADIENT  # The only method available is CV_HOUGH_GRADIENT
            dp = scale_hct_accumulator_resolution.get()                          # The resolution of the accumumator.
            min_dist = max(img_bgr.shape[0], img_bgr.shape[1])   # The minimum distance between 2 circles.
            canny_edge_threshold = scale_hct_canny_edge_threshold.get()
            accumulator_threshold = scale_hct_accumulator_threshold.get()
            min_radius = scale_hct_min_radius.get()
            max_radius = scale_hct_max_radius.get()
            #circles = cv.HoughCircles(img_mask, method, dp, min_dist)
            circles = cv.HoughCircles(img_mask, method, dp, min_dist, param1=canny_edge_threshold, param2=accumulator_threshold, minRadius=min_radius, maxRadius=max_radius)

            # DRAW CIRCLES ####################################

            if circles is not None:
                circles = np.uint16(np.around(circles))
                for i in circles[0,:]:
                    # draw the outer circle
                    cv.circle(img_bgr,(i[0],i[1]),i[2],(0,255,0),2)

                    # draw the center of the circle
                    cv.circle(img_bgr,(i[0],i[1]),2,(0,0,255),3)

            # DISPLAY IMAGES ##################################

            # Display the resulting frame (Mask)
            cv.imshow('Mask', img_mask)

            # Display the resulting frame (BGR)
            cv.imshow('BGR', img_bgr)

            # KEYBOARD LISTENER ###############################

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

    # Run the OpenCV main loop in a separate thread
    thread_cv = threading.Thread(target=opencv_main_loop)
    thread_cv.start()

    # Run the tkinter main loop
    root.mainloop()

    # Exit
    video_capture.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
