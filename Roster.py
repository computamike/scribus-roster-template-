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
import os
def copyPlayer(sourceName, destinationName):
    if scribus.objectExists(sourceName):
        doc = scribus.getDocName()
        unit = scribus.getUnit()
        (PageWidth,PageHeight) = scribus.getPageSize()
        (iT, iI, iO , iB) = scribus.getPageMargins()
        NewPagepoint = PageHeight - iT -iB
        player = scribus.selectObject(sourceName)
        #Duplicate the object...
        scribus.duplicateObject(sourceName)
        x = scribus.getSelectedObject()
        newObjectName = str(x)
        size = scribus.getSize(newObjectName)
        scribus.moveObject(0,size[1],newObjectName)
        (x,y) = scribus.getPosition(newObjectName)
        scribus.setRedraw(1)
        scribus.docChanged(1)
        if (y+size[1] > NewPagepoint):
            currentPage = scribus.currentPage()
            scribus.newPage(-1)
            newPage =  currentPage+1
            scribus.copyObject(newObjectName)
            scribus.deleteObject(newObjectName)
            scribus.gotoPage(newPage)
            scribus.pasteObject(newObjectName)
            scribus.moveObjectAbs(iO,iT,newObjectName)
        scribus.setNewName(destinationName,sourceName)
        scribus.setNewName(sourceName,newObjectName)

def main(argv):
    """This is a documentation string. Write a description of what your code
    does here. You should generally put documentation strings ("docstrings")
    on all your Python functions."""
    #########################
    #  YOUR CODE GOES HERE  #
    #########################
    #copyPlayer("__player__","PLAYER 1")
    #copyPlayer("__player__","PLAYER 2")
    #copyPlayer("__player__","PLAYER 3")
    csv = scribus.fileDialog('Open input', 'CSV files (*.csv)')
    stuff = {'NAME': 'Mike Hingley', 'ADDRESS': '22 Trinity Street, Cradley Heath, West Midlands' , 'PHOTO' : '128.jpg'}
    print(os.path.dirname(os.path.realpath(sys.argv[0])))
    print os.getcwd()
    print(sys.path[0])
    print(os.path.abspath(''))
    sourceName = "__player__"
    if scribus.objectExists(sourceName):
        scribus.selectObject(sourceName)
        scribus.unGroupObject()
        childObjectCount = scribus.selectionCount()
        for x in range(0, childObjectCount):
            element = scribus.getSelectedObject(x)
            if scribus.getObjectType(str(element))  == 'TextFrame':
                current = scribus.getAllText(element)
                if current in stuff:
                     fontsize = scribus.getFontSize(element)
                     font = scribus.getFont(element)
                     scribus.setText(stuff[current],element)
                     scribus.setFont(font)
                     scribus.setFontSize(fontsize)
            if scribus.getObjectType(str(element))  == 'ImageFrame':
                current = scribus.getImageFile(element)
                currentName = os.path.basename(os.path.normpath(current))
                print current
                print currentName
                if currentName in stuff:
                     ExistingFolder = os.path.split(current)
                     print ExistingFolder[0]
                     newFile = os.path.join(ExistingFolder[0],stuff[currentName])
                     print newFile
                     scribus.loadImage(newFile,element)
            print scribus.getObjectType(str(element))
            print str(scribus.getSelectedObject(x))
        scribus.groupObjects()
        print "name = " + scribus.getSelectedObject()
        scribus.setNewName("__player__",scribus.getSelectedObject())

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