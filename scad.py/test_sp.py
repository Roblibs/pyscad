from solid import *
from solid.utils import *  # Not required, but the utils module is useful

cs = cube(10, center = True) - up(5)(sphere(5))

out = up(5)(cs)

scad_render_to_file(out, "../scad/" + __file__ + ".scad")
