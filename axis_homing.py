
# my current version of FreeCAD uses python2
from __future__ import print_function

import os
import sys

from decimal import Decimal


# local module
import changer



# Detect if we are running directly or within FreeCAD
if __name__ == '__main__':
    # This is officially not recommended, see:
    # https://www.freecadweb.org/wiki/Embedding_FreeCAD#Caveats
    #
    # Should probably get FreeCAD in the PYTHONPATH from outside of the
    # script instead of hardcoding here.
    FREECADPATH= '/usr/lib/freecad/lib'
    sys.path.append(FREECADPATH)

    # Get the argument from the command line
    try:
        diameter = Decimal(sys.argv[1])
    except:
        print(sys.argv)
        print('ERROR: bad.  Argument expects desired diameter in mm.')
        raise

else:
    # We are running as a FreeCAD script, possibly invoked as
    # $ freecadcmd scriptname.py
    #
    # Get the argument via an environment variable instead
    #   (is there a better way?)
    try:
        diameter = Decimal(os.environ['FREECAD_AXIS_DIAMETER'])
    except:
        print(sys.argv)
        print('ERROR: bad.  Argument expects desired diameter in mm.')
        raise


# now we can reliably import the package
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



# Now everything is setup.  We are assuming at this point that `diameter` is a
# Decimal instance and already set.

# Do the deed and output files
part = AxisHoming()
part.changeAxisDiameter(diameter)
part.saveFreecad()
part.saveSTL()
