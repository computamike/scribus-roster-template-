#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    # Please do not use 'from scribus import *' . If you must use a 'from import',
    # Do so _after_ the 'import scribus' and only import the names you need, such
    # as commonly used constants.
    import scribus
except ImportError,err:
    print "This Python script is written for the Scribus scripting interface."
    print "It can only be run from within Scribus."
    sys.exit(1)

#########################
# YOUR IMPORTS GO HERE  #
#########################



def main(argv):
    """This is a documentation string. Write a description of what your code
    does here. You should generally put documentation strings ("docstrings")
    on all your Python functions."""
    #########################
    #  YOUR CODE GOES HERE  #
    #########################
    doc = scribus.getDocName()
    unit = scribus.getUnit()
    (PageWidth,PageHeight) = scribus.getPageSize()
    (iT, iI, iO , iB) = scribus.getPageMargins()
    NewPagepoint = PageHeight - iT -iB
    print iT
    print iI
    print iO
    print iB
    print unit
    print NewPagepoint
#print dir(doc)# Add a page
    #scribus.newPage(-1)
    if scribus.objectExists("__player__"):
        player = scribus.selectObject("__player__")
        #Duplicate the object...
        scribus.duplicateObject("__player__")
        x = scribus.getSelectedObject()
        newObjectName = str(x)
        size = scribus.getSize(newObjectName)
        scribus.moveObject(0,size[1],newObjectName)
        (x,y) = scribus.getPosition(newObjectName)
        scribus.setRedraw(1)
        scribus.docChanged(1)
        if (y+size[1] > NewPagepoint):
            currentPage = scribus.currentPage()
            print('CP: 0')
            scribus.newPage(-1)
            print('CP: 1')
            newPage =  currentPage+1
            print "current page = " + str(currentPage)
            print "New Page" + str(newPage)
            print('CP: 2')
            print "Copying object"  + newObjectName
            scribus.copyObject(newObjectName)
            scribus.deleteObject(newObjectName)
            scribus.gotoPage(newPage)
            scribus.pasteObject(newObjectName)
        #scribus.setNewName("PLAYER_1","__player__")
        #scribus.setNewName("__player__",str(x))


def main_wrapper(argv):
    """The main_wrapper() function disables redrawing, sets a sensible generic
    status bar message, and optionally sets up the progress bar. It then runs
    the main() function. Once everything finishes it cleans up after the main()
    function, making sure everything is sane before the script terminates."""
    try:
        scribus.statusMessage("Running script...")
        scribus.progressReset()
        main(argv)
    finally:
        # Exit neatly even if the script terminated with an exception,
        # so we leave the progress bar and status bar blank and make sure
        # drawing is enabled.
        if scribus.haveDoc():
            scribus.setRedraw(True)
        scribus.statusMessage("")
        scribus.progressReset()

# This code detects if the script is being run as a script, or imported as a module.
# It only runs main() if being run as a script. This permits you to import your script
# and control it manually for debugging.
if __name__ == '__main__':
    main_wrapper(sys.argv)