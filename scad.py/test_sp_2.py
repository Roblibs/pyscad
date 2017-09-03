from solid import *
from solid.utils import *  # Not required, but the utils module is useful

d = cube(5) + right(5)(sphere(5)) - cylinder(r=2, h=6)
scad_render_to_file(d, "../scad/" + __file__ + ".scad")
