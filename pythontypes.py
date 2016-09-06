#!/usr/bin/env python

###################################################
#            Picraft @ Impulse Labs               #
#           http://www.impulselabs.io             #
###################################################

import mcpi.minecraft as minecraft
import mcpi.block as block

#mc = minecraft.Minecraft.create()
myObject = {"number": 20, "decimal": 2.5, "Text": "Hello you", "List": [3, 6, 9]}
#print ('mc is of type: ' + type(mc))
print ('myObject is: '  + str(type(myObject)))
print ('number is: ' + str(type(myObject["number"])))
print ('decimal is: ' + str(type(myObject["decimal"])))
print ('text is: ' + str(type(myObject["Text"])))
print ('list is: ' + str(type(myObject["List"])))
