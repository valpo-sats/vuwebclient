
import os
import sys


# should probably get FreeCAD in the PYTHONPATH from outside of the script
FREECADPATH= '/usr/lib/freecad/lib'
sys.path.append(FREECADPATH)

import FreeCAD
import Mesh


class Changer(object):
    def __init__(self, name):
        self.name = name
        FreeCAD.open('satnogs-rotator/rotator_parts/' + self.name + '.fcstd')
        self.doc = FreeCAD.ActiveDocument

    def saveFreecad(self):
        """Save the modified part as a new FreeCAD file."""
        # TODO: handle arbitrary path+names
        self.doc.saveAs(os.getcwd() + os.path.sep + self.outname + '.fcstd')

    def saveSTL(self):
        """Export the modified part as a STL file."""
        # Export an STL of the part
        objs = []
        objs.append(self.doc.getObject(self.stl_object))
        Mesh.export(objs, self.outname + '.stl')

