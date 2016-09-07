#! /usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

def drawTrap(locx, locy, locz, size, blockId, blockData):
    mc.setBlocks(locx + 1, locy-1, locz + 1, locx + size, locy-1, locz + size, blockId, blockData)


if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    orig = mc.player.getTilePos()
    drawTrap( orig.x, orig.y, orig.z, 3, block.COBWEB.id, block.COBWEB.data)

    while True:
        time.sleep(2)
        pos = mc.player.getTilePos()
        if pos.x > orig.x and pos.x < orig.x + 3 + 1 and pos.z > orig.z and pos.z < orig.z + 3 + 1:
            print("x="+str(pos.x) + " y="+str(pos.y) + " z="+str(pos.z))
            mc.postToChat("Welcome to the cobweb trap!")
