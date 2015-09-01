# -*- coding: utf-8 -*-

# VoR12

# The MIT License
#
# Copyright (c) 2015 Jeremie DECOCK (http://www.jdhp.org)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import print_function

__all__ = ['RuleBasedController']

import cv2 as cv
import numpy as np

# Ratio of the motionless area on the image width
# (should be between 0.0 and 1.0)
MOTIONLESS_AREA_X_RATIO = 0.3

# Ratio of the motionless area on the image height
# (should be between 0.0 and 1.0)
MOTIONLESS_AREA_Y_RATIO = 0.3

class RuleBasedController(object):

    def __init__(self, image_width, image_height):
        motionless_area_width = image_width * MOTIONLESS_AREA_X_RATIO
        motionless_area_height = image_height * MOTIONLESS_AREA_Y_RATIO

        motionless_area_x1 = int((image_width - motionless_area_width)/2)
        motionless_area_x2 = int(image_width - (image_width - motionless_area_width)/2)

        motionless_area_y1 = int((image_height - motionless_area_height)/2)
        motionless_area_y2 = int(image_height - (image_height - motionless_area_height)/2)

        self.motionless_area_range_x = (motionless_area_x1, motionless_area_x2)
        self.motionless_area_range_y = (motionless_area_y1, motionless_area_y2)


    def compute_control(self, percept):
        target_center = np.array([percept[0], percept[1]])

        # Control on the x axis (left/right position)
        ctrl_x = 0
        if target_center[0] < self.motionless_area_range_x[0]:
            ctrl_x = -1
        elif target_center[0] > self.motionless_area_range_x[1]:
            ctrl_x = 1

        # Control on the y axis (up/down position)
        # Warning: with OpenCV, the y axis is inverted (i.e. 0 is at the top)!
        ctrl_y = 0
        if target_center[1] < self.motionless_area_range_y[0]:
            ctrl_y = 1
        elif target_center[1] > self.motionless_area_range_y[1]:
            ctrl_y = -1

        # Control vect
        control_vect = np.array([ctrl_x, ctrl_y])

        return control_vect


    def draw_image(self, image, control_vect):
        # TODO: move this in the main script ?

        # Draw the motionless area
        color = (0, 0, 255)
        thickness = 1
        point1 = (self.motionless_area_range_x[0],
                  self.motionless_area_range_y[0])
        point2 = (self.motionless_area_range_x[1],
                  self.motionless_area_range_y[1])
        cv.rectangle(image, point1, point2, color, thickness)

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
            cv.putText(image, ctrl_text, start_point, font, font_scale, color,
                       thickness, line_type)

