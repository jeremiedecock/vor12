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

from pyax12.connection import Connection

__all__ = ['DynamixelAX12']

class DynamixelAX12(object):

    def __init__(self):

        # Connect to the serial port
        self.connection = Connection(port="/dev/ttyUSB0", baudrate=57600)

        self.dynamixel_x_axis_id = 3
        self.dynamixel_z_axis_id = 4

        # Setup the angle limits fot the X axis
        self.connection.set_cw_angle_limit(self.dynamixel_x_axis_id, -90,
                                           degrees=True)
        self.connection.set_ccw_angle_limit(self.dynamixel_x_axis_id, 90,
                                            degrees=True)

        # Setup the angle limits fot the Z axis
        self.connection.set_cw_angle_limit(self.dynamixel_z_axis_id, -90,
                                           degrees=True)
        self.connection.set_ccw_angle_limit(self.dynamixel_z_axis_id, 90,
                                            degrees=True)

        # Goto the initial position (0°)
        self.connection.goto(self.dynamixel_x_axis_id, 0, speed=512,
                             degrees=True)
        self.connection.goto(self.dynamixel_z_axis_id, 0, speed=512,
                             degrees=True)

        # TODO: set CW_ANGLE_LIMIT and CCW_ANGLE_LIMIT (+ alarms)
        #       (+ memorize the original values to set them back)


    def __del__(self):
        # TODO: set CW_ANGLE_LIMIT and CCW_ANGLE_LIMIT (+ alarms)

        # Goto the initial position (0°)
        self.connection.goto(self.dynamixel_x_axis_id, 0, speed=512,
                             degrees=True)
        self.connection.goto(self.dynamixel_z_axis_id, 0, speed=512,
                             degrees=True)

        # Setup the angle limits fot the X axis
        self.connection.set_cw_angle_limit(self.dynamixel_x_axis_id,
                                           -150, degrees=True)
        self.connection.set_ccw_angle_limit(self.dynamixel_x_axis_id,
                                            150, degrees=True)

        # Setup the angle limits fot the Z axis
        self.connection.set_cw_angle_limit(self.dynamixel_z_axis_id,
                                           -150, degrees=True)
        self.connection.set_ccw_angle_limit(self.dynamixel_z_axis_id,
                                            150, degrees=True)

        self.connection.close()


    def apply_control(self, control_vect):
        print(control_vect)

        pos_x = self.connection.get_present_position(self.dynamixel_x_axis_id)
        pos_z = self.connection.get_present_position(self.dynamixel_z_axis_id)

        # The x_axis controls up/down movements
        new_pos_x = pos_x - (int(control_vect[1]) * 10)

        # The z_axis controls left/right movements
        # Warning: movements are inverted on the z axis
        #          (negative commands move the frame to the right)
        new_pos_z = pos_z - (int(control_vect[0]) * 10)

        #try:
        self.connection.goto(self.dynamixel_x_axis_id, new_pos_x, speed=512)
        self.connection.goto(self.dynamixel_z_axis_id, new_pos_z, speed=512)
        #except ...:
        #    pass

