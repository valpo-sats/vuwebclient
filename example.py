
# my current version of FreeCAD uses python2

import os
import sys

# should probably get FreeCAD in the PATH from outside of the script
FREECADPATH= '/usr/lib/freecad/lib'
sys.path.append(FREECADPATH)

import FreeCAD as fc
import Mesh

fc.open('foo.fcstd')

doc = fc.ActiveDocument

# All we really need
# ... short of checking assumptions and valid ranges
doc.Sketch.setDatum('InsideRadius', fc.Units.Quantity('30 mm'))
doc.recompute()

# output the modified file
doc.saveAs(os.getcwd() + os.path.sep + 'modified.fcstd')


# Export an STL of the part
# TODO: select the correct object for proper export
objs = []
objs.append(doc.getObject('Pad'))
Mesh.export(objs, './modified.stl')

