#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2015 Jérémie DECOCK (http://www.jdhp.org)

"""
Vor12

Required: opencv library (Debian: aptitude install python-opencv)
"""

from __future__ import print_function

import argparse
import cv2 as cv

import computer_vision.circle_detection as circle_detection
import controler.rules_based_controler as rules_based_controler

def main():

    # Parse the programm options (get the path of the image file to read) #####

    parser = argparse.ArgumentParser(description='An opencv snippet.')
    parser.add_argument("--cameraid", "-i", help="The camera ID number (default: 0)", type=int, default=0, metavar="INTEGER")
    args = parser.parse_args()

    device_number = args.cameraid

    # OpenCV ##################################################################

    camera = circle_detection.CircleDetection(device_number)
    
    (image_width, image_height) = camera.get_image_size()
    controler = rules_based_controler.RulesBasedController(image_width, image_height)

    print("Press q to quit.")

    while True:

        # GET PERCEPTS ####################################

        percept_vect = camera.get_percept()
        control_vect = None

        if percept_vect is not None:

            # FILTER PERCEPTS #################################

            # TODO
            #percept_vect = filtrer(percept_vect)

            # COMPUTE CONTROL #################################

            control_vect = controler.compute_control(percept_vect)
            print(control_vect)

            # FILTER CONTROL ##################################

            # TODO
            #control_vect = filtrer(control_vect)

            # APPLY CONTROL ###################################

            # TODO
            #actuator.apply_control(control_vect)


        # SHOW IMAGES #####################################

        # Add informations on images
        camera.draw_image(camera.img_bgr, percept_vect)
        controler.draw_image(camera.img_bgr, control_vect)

        # Display the resulting frame (Mask)
        cv.imshow('Mask', camera.img_mask)

        # Display the resulting frame (BGR)
        cv.imshow('BGR', camera.img_bgr)


        # KEYBOARD LISTENER ###############################

        if cv.waitKey(1) & 0xFF == ord('q'):
            # Exit
            break


if __name__ == '__main__':
    main()

