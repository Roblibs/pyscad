

union() {
	translate(v = [-5, 0, 0]) {
		cube(size = 10);
	}
	sphere(r = 8);
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
from solid import *
from solid.utils import *  # Not required, but the utils module is useful

py_scad_obj_2 = left(5)( cube(10) ) + sphere(8)

scad_render_to_file(py_scad_obj_2, "../scad/" + __file__ + ".scad")
 
 
************************************************/
