# pyscad
3d objects using scad with generation from [solid python](http://solidpython.readthedocs.io/en/latest/)

# How to live preview ?
- simply double click the auto_update.bat that will run the python script with the same name
- create any solidpython file in the scad.py directory
- save your file once to have the corresponding scad file with the same name created in the scad directory
- open the scad file with the [OpenScad](http://www.openscad.org/) Viewer
- Now work on your solidpython file, every time you save it, the auto_update will automatically run the modified python file that should always end with the 'scad_render_to_file' function, which itself creates the scad file that is automatically updated in the openscad viewer
