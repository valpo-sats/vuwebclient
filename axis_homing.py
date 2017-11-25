
# my current version of FreeCAD uses python2
from __future__ import print_function

import os
import sys

from decimal import Decimal

import changer

# should probably get FreeCAD in the PYTHONPATH from outside of the script
FREECADPATH= '/usr/lib/freecad/lib'
sys.path.append(FREECADPATH)

import FreeCAD
import Mesh



class AxisHoming(changer.Changer):
    def __init__(self):
        name = 'axis_homing'
        super(AxisHoming, self).__init__(name)

    def changeAxisDiameter(self, d):
        """Set a new diameter, in mm, for the thru axis tube."""
        self.diameter = Decimal(d)

        self.outname = 'output/' + self.name + '-%smm' % self.diameter

        self.stl_object = 'Chamfer001'  # select the correct object for STL export

        # change the central hole size from the spreadsheet
        # all other dependent parameters are keyed to this value in the model
        cell = self.doc.Spreadsheet.getCellFromAlias('AxisDiameter')
        self.doc.Spreadsheet.set(cell, str(self.diameter))

        # exceptions may be thrown here??
        self.doc.recompute()



if __name__ == '__main__':
    try:
        diameter = Decimal(sys.argv[1])
    except:
        print(sys.argv)
        print('ERROR: bad.  Argument expects desired diameter in mm.')
        raise

    part = AxisHoming()
    part.changeAxisDiameter(diameter)
    part.saveFreecad()
    part.saveSTL()
