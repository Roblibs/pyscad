

difference() {
	union() {
		cube(size = 5);
		translate(v = [5, 0, 0]) {
			sphere(r = 5);
		}
	}
	cylinder(h = 6, r = 2);
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
from solid import *
from solid.utils import *  # Not required, but the utils module is useful

d = cube(5) + right(5)(sphere(5)) - cylinder(r=2, h=6)
scad_render_to_file(d, "../scad/" + __file__ + ".scad")
 
 
************************************************/
