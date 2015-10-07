// VoR-12 - 2D foot

// Copyright (c) 2015 Jérémie DECOCK (www.jdhp.org)

// Base unit: mm

module 2d_foot() {
    inner_square_size = 33;
    outer_square_size = 105;
    screw_hole_diameter = 3;

    difference() {
        union() {
            square(outer_square_size, center=true);
            rotate(45) 2d_toe();
            rotate(135) 2d_toe();
            rotate(-45) 2d_toe();
            rotate(-135) 2d_toe();
        }

        union() {
            square(inner_square_size, center=true);
            translate([-31.5,    0]) circle(d=screw_hole_diameter);
            translate([ 31.5,    0]) circle(d=screw_hole_diameter);
            translate([    0, 38.5]) circle(d=screw_hole_diameter);
        }
    }
}

module 2d_toe() {
    $fn=50;

    toe_depth = 25;
    toe_length = 80;

    hull() {
        square(toe_depth, center=true);
        translate([toe_length, 0]) circle(d=toe_depth);
    }
}

// Uncomment the following line to test this module
2d_foot();
