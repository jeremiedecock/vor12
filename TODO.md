# TODO

## Vor12-A

- [ ] Control
    - [ ] Let pyax12 works as an external library
    - [ ] Write a first simple controller: if the center is out of a given window, go to that direction
    - [ ] Proportional move: setup moving speed with the distance of the ball to the center of the screen
    - [ ] Try PID control ?
- [ ] Computer vision
    - [x] Add the Hough Circle Transform calibration script
    - [x] Add the computer vision script
    - [x] Add text informations in OpenCV windows: circle center and radius, draw the non-react window
    - [ ] Add filters (erode, ...)
    - [ ] Try other params (accumulator resolution, ...): see what other people do on internet
- [ ] Add a Kalman filter to stabilize the sensor input (create a generic
      SensorFilter class to try other filters like particle filters)
- [ ] Make longer Dynamixel cables
- [ ] Add Kicad files
- [ ] Add OpenSCAD files

## Vor12-B

- [ ] Replace Dynamixels AX-12 by Dynamixel XL-320 actuators

## Vor12-C

- [ ] Replace Dynamixels AX-12 by standard cheap servomotors (those controled by PWM and without state feedback)
- [ ] Use a RaspberryPi and a Raspicam

## Mid-term and long-term TODO list

- [ ] Use other computer vision algorithms (pattern search, ...)

