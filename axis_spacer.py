
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



class AxisSpacer(changer.Changer):
    def __init__(self):
        name = 'axis_spacer'
        super(AxisSpacer, self).__init__(name)

    def changeAxisDiameter(self, d):
        """Set a new diameter, in mm, for the thru axis tube."""
        self.diameter = Decimal(d)

        self.outname = 'output/' + self.name + '-%smm' % self.diameter

        self.stl_object = 'Pad'  # select the correct object for STL export

        # change the central hole size
        radius = self.diameter / Decimal('2.00')
        print('radius:', radius)
        self.doc.Sketch.setDatum('AxisRadius', FreeCAD.Units.Quantity('%s mm' % radius))

        # exceptions may be thrown here??
        self.doc.recompute()



if __name__ == '__main__':
    try:
        diameter = Decimal(sys.argv[1])
    except:
        print(sys.argv)
        print('ERROR: bad.  Argument expects desired diameter in mm.')
        raise

    part = AxisSpacer()
    part.changeAxisDiameter(diameter)
    part.saveFreecad()
    part.saveSTL()
