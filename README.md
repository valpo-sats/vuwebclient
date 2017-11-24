# satnogs-partchanger

These utilities modify SatNOGS Rotator parts to fit locally-available tubing materials.  It removes the need to be personally knowledgeable about using FreeCAD to modify the source files to change the relevant parts of the 3D models.

Input the desired diameter of your tubing in milimeters and you get new `.stl` and `.fcstd` files for the following parts:

* `axis_spacer`
* `axis_gear_flange`


## Development notes

This repository uses a `git submodule`.  When initially cloning, use:

    `git clone --recursive`

and/or, anytime afterwards use the following to keep the submodule updated:

    `git submodule update --init`
