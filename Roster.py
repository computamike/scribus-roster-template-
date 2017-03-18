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
    #print dir(doc)# Add a page
    #scribus.newPage(-1)
    if scribus.objectExists("__player__"):
        print "Found Object : __player__"
        player = scribus.selectObject("__player__")
        print "here ok"
        #from scribus import *
        print player.names
        print "cp2"
        #scribus.unGroupObject("__player__")
        print dir(player)
        #print player.names
        #newNames = []
        #for name in player.names:
        #    print name
        #    x = scribus.duplicateObject(name)
        #    x.name = name + "_COPY"
        #    x.moveObject(0,100,scribus.selectObject(x.name ))
        #    newNames.append(x.name)
        # regroup __Player__
        #scribus.groupObjects(player.names)
        #newGroup =  scribus.groupObjects(newNames)
        #newGroup.name = "foobar"
        scribus.redrawAll()
    print "Processing document " + doc
#
#    ['%', 'ALIGN_BLOCK', 'ALIGN_CENTERED', 'ALIGN_FORCED', 'ALIGN_LEFT',
#    'ALIGN_RIGHT', 'BUTTON_ABORT', 'BUTTON_CANCEL', 'BUTTON_IGNORE',
#    'BUTTON_NO', 'BUTTON_NONE', 'BUTTON_OK', 'BUTTON_RETRY', 'BUTTON_YES',
#    'CAP_FLAT', 'CAP_ROUND', 'CAP_SQUARE', 'COLOR', 'COLOR_BURN', 'COLOR_DODGE',
#    'DARKEN', 'DIFFERENCE', 'EXCLUSION', 'FACINGPAGES', 'FILL_CROSSDIAGONALG',
#    'FILL_DIAGONALG', 'FILL_HORIZONTALG', 'FILL_NOG', 'FILL_RADIALG',
#    'FILL_VERTICALG', 'FIRSTPAGELEFT', 'FIRSTPAGERIGHT', 'HARD_LIGHT', 'HUE',
#    'ICON_CRITICAL', 'ICON_INFORMATION', 'ICON_NONE', 'ICON_WARNING',
#    'ImageExport', 'JOIN_BEVEL', 'JOIN_MITTER', 'JOIN_ROUND', 'LANDSCAPE',
#    'LIGHTEN', 'LINE_DASH', 'LINE_DASHDOT', 'LINE_DASHDOTDOT', 'LINE_DOT',
#    'LINE_SOLID', 'LUMINOSITY', 'MULTIPLY', 'NOFACINGPAGES', 'NORMAL',
#    'NameExistsError', 'NoDocOpenError', 'NoValidObjectError',
#    'NotFoundError', 'OVERLAY', 'PAGE_1', 'PAGE_2', 'PAGE_3', 'PAGE_4',
#    'PAPER_A0', 'PAPER_A1', 'PAPER_A2', 'PAPER_A3', 'PAPER_A4', 'PAPER_A5',
#    'PAPER_A6', 'PAPER_A7', 'PAPER_A8', 'PAPER_A9', 'PAPER_B0', 'PAPER_B1',
#    'PAPER_B10', 'PAPER_B2', 'PAPER_B3', 'PAPER_B4', 'PAPER_B5', 'PAPER_B6',
#    'PAPER_B7', 'PAPER_B8', 'PAPER_B9', 'PAPER_C5E', 'PAPER_COMM10E', 'PAPER_DLE',
#    'PAPER_EXECUTIVE', 'PAPER_FOLIO', 'PAPER_LEDGER', 'PAPER_LEGAL',
#    'PAPER_LETTER', 'PAPER_TABLOID', 'PDFfile', 'PORTRAIT', 'Printer',
#    'SATURATION', 'SCREEN', 'SOFT_LIGHT', 'ScribusException', 'UNIT_C',
#    'UNIT_CENTIMETRES', 'UNIT_CICERO', 'UNIT_CM', 'UNIT_IN', 'UNIT_INCHES',
#    'UNIT_MILLIMETERS', 'UNIT_MM', 'UNIT_P', 'UNIT_PICAS', 'UNIT_POINTS',
#    'UNIT_PT', 'WrongFrameTypeError', '__builtin__', '__doc__', '__name__',
#     '__package__', '_bu', '_ia', 'c', 'changeColor', 'closeDoc',
#    'closeMasterPage', 'cm', 'createBezierLine', 'createCharStyle',
#    'createEllipse', 'createImage', 'createLayer', 'createLine',
#    'createMasterPage', 'createParagraphStyle', 'createPathText',
#    'createPolyLine', 'createPolygon', 'createRect', 'createText',
#    'currentPage', 'defineColor', 'dehyphenateText', 'deleteColor',
#    'deleteLayer', 'deleteMasterPage', 'deleteObject', 'deletePage',
#    'deleteText', 'deselectAll', 'docChanged', 'duplicateObject', 'editMasterPage',
#    'exceptions', 'fileDialog', 'fileQuit', 'getActiveLayer', 'getAllObjects',
#    'getAllStyles', 'getAllText', 'getColor', 'getColorAsRGB', 'getColorNames',
#    'getColumnGap', 'getColumns', 'getCornerRadius', 'getDocName',
#    'getFillBlendmode', 'getFillColor', 'getFillShade', 'getFillTransparency',
#    'getFont', 'getFontNames', 'getFontSize', 'getGuiLanguage', 'getHGuides',
#    'getImageFile', 'getImageScale', 'getLayerBlendmode',
#    'getLayerTransparency', 'getLayers', 'getLineBlendmode', 'getLineCap',
#    'getLineColor', 'getLineJoin', 'getLineShade', 'getLineSpacing',
#    'getLineStyle', 'getLineTransparency', 'getLineWidth', 'getObjectType',
#    'getPageItems', 'getPageMargins', 'getPageNMargins', 'getPageNSize',
#    'getPageSize', 'getPageType', 'getPosition', 'getProperty',
#    'getPropertyCType', 'getPropertyNames', 'getRotation',
#    'getSelectedObject', 'getSize', 'getText', 'getTextColor',
#    'getTextDistances', 'getTextLength', 'getTextLines', 'getTextShade',
#    'getUnit', 'getVGuides', 'getXFontNames', 'getval', 'gotoPage',
#    'groupObjects', 'haveDoc', 'hyphenateText', 'importPage', 'inch',
#    'insertText', 'isLayerFlow', 'isLayerLocked', 'isLayerOutlined',
#    'isLayerPrintable', 'isLayerVisible', 'isLocked', 'isPDFBookmark',
#    'isSpotColor', 'linkTextFrames', 'loadImage', 'loadStylesFromFile',
#    'lockObject', 'mainWindow', 'masterPageNames', 'messageBox',
#    'messagebarText', 'mm', 'moveObject', 'moveObjectAbs',
#    'moveSelectionToBack', 'moveSelectionToFront', 'newDoc', 'newDocDialog',
#    'newDocument', 'newPage', 'newStyleDialog', 'objectExists',
#    'openDoc', 'p', 'pageCount', 'pageDimension', 'placeEPS', 'placeODG',
#    'placeSVG', 'placeSXD', 'progressReset', 'progressSet', 'progressTotal',
#    'pt', 'qApp', 'redrawAll', 'renderFont', 'replaceColor', 'retval',
#    'rotateObject', 'rotateObjectAbs', 'saveDoc', 'saveDocAs',
#    'savePageAsEPS', 'scaleGroup', 'scaleImage', 'scribus_version',
#    'scribus_version_info', 'scrollDocument', 'selectObject', 'selectText',
#    'selectionCount', 'sentToLayer', 'setActiveLayer', 'setColumnGap',
#    'setColumns', 'setCornerRadius', 'setCursor', 'setDocType',
#    'setFillBlendmode', 'setFillColor', 'setFillShade', 'setFillTransparency',
#    'setFont', 'setFontSize', 'setGradientFill', 'setGradientStop',
#    'setHGuides', 'setImageOffset', 'setImageScale', 'setInfo',
#    'setLayerBlendmode', 'setLayerFlow', 'setLayerLocked', 'setLayerOutlined',
#    'setLayerPrintable', 'setLayerTransparency', 'setLayerVisible',
#    'setLineBlendmode', 'setLineCap', 'setLineColor', 'setLineJoin',
#    'setLineShade', 'setLineSpacing', 'setLineStyle', 'setLineTransparency',
#    'setLineWidth', 'setMargins', 'setMultiLine', 'setNewName',
#    'setPDFBookmark', 'setProperty', 'setRedraw', 'setScaleImageToFrame',
#    'setSpotColor', 'setStyle', 'setText', 'setTextAlignment', 'setTextColor',
#    'setTextDistances', 'setTextScalingH', 'setTextScalingV', 'setTextShade',
#    'setTextStroke', 'setUnit', 'setVGuides', 'sizeObject', 'statusMessage',
#    'textFlowMode', 'textOverflows', 'traceText', 'unGroupObject',
#    'unlinkTextFrames', 'valueDialog', 'warnings',
#    'zoomDocument', '\xb0']
#Processing document /home/mike/Resume.sla

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