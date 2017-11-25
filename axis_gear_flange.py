
# my current version of FreeCAD uses python2
from __future__ import print_function

import os
import sys

from decimal import Decimal

import changer



class AxisGearFlange(changer.Changer):
    def __init__(self):
        name = 'axis_gear_flange'
        super(AxisGearFlange, self).__init__(name)

    def changeAxisDiameter(self, d):
        """Set a new diameter, in mm, for the thru axis tube."""
        self.diameter = Decimal(d)

        self.outname = 'output/' + self.name + '-%smm' % self.diameter

        self.stl_object = 'Fillet'  # select the correct object for STL export

        # change the central hole size
        radius = self.diameter / Decimal('2.000')
        print('radius:', radius)
        self.doc.Sketch.setDatum('AxisRadius', FreeCAD.Units.Quantity('%s mm' % radius))

        # update the M3 nut internal pockets
        # inset by 3.5mm (max nut thickness is 2.4mm by spec)
        inset = Decimal('3.5')
        padLength = Decimal('2.0') * inset + self.diameter
        self.doc.getObjectsByLabel('Pad-M3Nut')[0].Length = '%s mm' % padLength
        self.doc.getObjectsByLabel('Pad-M3Nut1')[0].Length = '%s mm' % padLength

        # exceptions may be thrown here??
        self.doc.recompute()



if __name__ == '__main__':
    try:
        diameter = Decimal(sys.argv[1])
    except:
        print(sys.argv)
        print('ERROR: bad.  Argument expects desired diameter in mm.')
        raise

    part = AxisGearFlange()
    part.changeAxisDiameter(diameter)
    part.saveFreecad()
    part.saveSTL()
