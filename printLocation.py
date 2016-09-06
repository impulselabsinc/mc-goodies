#!/usr/bin/env python

###################################################
#            Picraft @ Impulse Labs               #
#           http://www.impulselabs.io             #
###################################################

# Tell the application which files you are going to use
# (I want to use a phone to call minecraft television studio)
import mcpi.minecraft as minecraft

# Open a connection to Minecraft and store the connection in memory
# (I dial the number for the minecraft television studio and keep the line open)
mc = minecraft.Minecraft.create()

# Use the connection to get information about the in-game character (you)
# (I ask the actor at the other end of the line to tell me how far he is from the camera)
# (I write down what he tells me on a piece of paper)
pos = mc.player.getTilePos()

# Display the information stored in memory on the screen
print("x="+str(pos.x) + " y="+str(pos.y) + " z="+str(pos.z))

# Discussion: Types
# What would happen if we do not put str() around the numbers?
