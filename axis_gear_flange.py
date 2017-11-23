
# my current version of FreeCAD uses python2

import os
import sys

# should probably get FreeCAD in the PYTHONPATH from outside of the script
FREECADPATH= '/usr/lib/freecad/lib'
sys.path.append(FREECADPATH)

import FreeCAD
import Mesh


NAME = 'axis_gear_flange'

FreeCAD.open('satnogs-rotator/rotator_parts/' + NAME + '.fcstd')

doc = FreeCAD.ActiveDocument

# All we really need
# ... short of checking assumptions and valid ranges
doc.Sketch.setDatum('AxisRadius', FreeCAD.Units.Quantity('10 mm'))
doc.recompute()

# output the modified file
doc.saveAs(os.getcwd() + os.path.sep + NAME + '-mod.fcstd')


# Export an STL of the part
# TODO: select the correct object for proper export
# objs = []
# objs.append(doc.getObject('Pad'))
# Mesh.export(objs, './modified.stl')

