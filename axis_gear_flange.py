
# my current version of FreeCAD uses python2
from __future__ import print_function

import os
import sys

from decimal import Decimal

# should probably get FreeCAD in the PYTHONPATH from outside of the script
FREECADPATH= '/usr/lib/freecad/lib'
sys.path.append(FREECADPATH)

import FreeCAD
import Mesh



# dimensions are in mm
newDiameter = Decimal('24.00')

NAME = 'axis_gear_flange'
OUTNAME = 'output/' + NAME + '-%smm' % newDiameter



FreeCAD.open('satnogs-rotator/rotator_parts/' + NAME + '.fcstd')
doc = FreeCAD.ActiveDocument

# change the central hole size
radius = newDiameter / 2
print('radius:', radius)
doc.Sketch.setDatum('AxisRadius', FreeCAD.Units.Quantity('%s mm' % radius))

# update the M3 nut internal pockets
# inset by 3.5mm (max nut thickness is 2.4mm by spec)
inset = Decimal('3.5')
padLength = Decimal('2.0') * inset + newDiameter
print('padLength:', padLength)
doc.getObjectsByLabel('Pad-M3Nut')[0].Length = '%s mm' % padLength
doc.getObjectsByLabel('Pad-M3Nut1')[0].Length = '%s mm' % padLength

# update the part
doc.recompute()

# output the modified file
doc.saveAs(os.getcwd() + os.path.sep + OUTNAME + '.fcstd')


# Export an STL of the part
# TODO: select the correct object for proper export
objs = []
objs.append(doc.getObject('Fillet'))
Mesh.export(objs, OUTNAME + '.stl')

