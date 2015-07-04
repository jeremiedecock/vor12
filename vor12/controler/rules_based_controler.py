# -*- coding: utf-8 -*-

# Copyright (c) 2015 Jérémie DECOCK (http://www.jdhp.org)

from __future__ import print_function

import cv2 as cv
import numpy as np

MOTIONLESS_AREA_X_RATIO = 0.3  # Ratio of the motionless area on the image width (should be between 0.0 and 1.0)
MOTIONLESS_AREA_Y_RATIO = 0.3  # Ratio of the motionless area on the image height (should be between 0.0 and 1.0)

class RulesBasedController(object):

    def __init__(self, image_width, image_height):
        motionless_area_width = image_width * MOTIONLESS_AREA_X_RATIO
        motionless_area_height = image_height * MOTIONLESS_AREA_Y_RATIO

        self.motionless_area_range_x = (int((image_width - motionless_area_width)/2),   int(image_width - (image_width - motionless_area_width)/2))
        self.motionless_area_range_y = (int((image_height - motionless_area_height)/2), int(image_height - (image_height - motionless_area_height)/2))


    def compute_control(self, percept):
        target_center = np.array([percept[0], percept[1]])

        # Control on the x axis
        ctrl_x = 0
        if target_center[0] < self.motionless_area_range_x[0]:
            ctrl_x = 1
        elif target_center[0] > self.motionless_area_range_x[1]:
            ctrl_x = -1

        # Control on the y axis
        ctrl_y = 0
        if target_center[1] < self.motionless_area_range_y[0]:
            ctrl_y = 1
        elif target_center[1] > self.motionless_area_range_y[1]:
            ctrl_y = -1

        # Control vect
        control_vect = np.array([ctrl_x, ctrl_y])

        return control_vect


    def draw_image(self, image, control_vect):

        # Draw the motionless area
        color = (0, 0, 255)
        thickness = 1
        cv.rectangle(image, (self.motionless_area_range_x[0], self.motionless_area_range_y[0]), (self.motionless_area_range_x[1], self.motionless_area_range_y[1]), color, thickness)

        # Draw the control
        if control_vect is not None:
            ctrl_text = ""

            if control_vect[1] > 0:
                ctrl_text += "up "
            elif control_vect[1] < 0:
                ctrl_text += "down "

            if control_vect[0] > 0:
                ctrl_text += "right"
            elif control_vect[0] < 0:
                ctrl_text += "left"

            start_point = (15, 100)
            font = cv.FONT_HERSHEY_SIMPLEX
            font_scale = 0.75
            color = (0, 0, 255)
            thickness = 2
            line_type = cv.CV_AA  # Anti-Aliased
            cv.putText(image, ctrl_text, start_point, font, font_scale, color, thickness, line_type)

