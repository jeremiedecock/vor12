# TODO

## Vor12-A

- [ ] Use the former description ("sentinel" project)
        track objects/animals/persons with a camera and 2 servomotors.

        Uses OpenCV for "target" detection and motor control.

        La partie "motor control" est très simple, pas besoin de cinematique inverce etc.
        il suffit de mesurer la distance x et y du centre de la cible au centre de l'écran
        et d'activer proportionellement les moteurs (commande en vitesse et non pas en position):

        command_motor_x = delta_x_target_center * a_fixed_coef
        command_motor_y = delta_y_target_center * a_fixed_coef
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
- [ ] Use a cross platform configuration file to save opencv calibration data
  (thresholds, ...) and pyax12 config (port, baudrate, ...)
- [ ] Add Kicad files
- [ ] Add OpenSCAD files

## Vor12-B

- [ ] Replace Dynamixels AX-12 by Dynamixel XL-320 actuators

## Vor12-C

- [ ] Replace Dynamixels AX-12 by standard cheap servomotors (those controled by PWM and without state feedback)
- [ ] Use a RaspberryPi and a Raspicam

## Mid-term and long-term TODO list

- [ ] Use other computer vision algorithms (pattern search, ...)

