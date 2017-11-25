
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

NAME = 'axis_homing'
OUTNAME = 'output/' + NAME + '-%smm' % newDiameter



FreeCAD.open('satnogs-rotator/rotator_parts/' + NAME + '.fcstd')
doc = FreeCAD.ActiveDocument

# change the central hole size from the spreadsheet
# all other dependent parameters are keyed to this value in the model
cell = doc.Spreadsheet.getCellFromAlias('AxisDiameter')
doc.Spreadsheet.set(cell, str(newDiameter))

# update the part
doc.recompute()

# output the modified file
doc.saveAs(os.getcwd() + os.path.sep + OUTNAME + '.fcstd')


# Export an STL of the part
# TODO: select the correct object for proper export
objs = []
objs.append(doc.getObject('Chamfer001'))
Mesh.export(objs, OUTNAME + '.stl')

