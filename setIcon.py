#!/usr/bin/python
from AppKit import NSWorkspace
from AppKit import NSImage
import sys
import glob
import os

NSWorkspace.sharedWorkspace().setIcon_forFile_options_(NSImage.alloc().initWithContentsOfFile_((sys.argv[1])), (sys.argv[2]), 0) or sys.exit(1)
