#Author: George Landon
#Tested with Maya 2018
#09/23/2018

#Select your poly object before executing mesh
#once executed, copy and paste into GLSL code

import maya.cmds as cmds
import maya.mel as mm

VERT_OUTPUT_NAME = 'CUBE_VERTS'
INDEX_OUTPUT_NAME = 'CUBE_INDEX'

selection = cmds.ls(selection=True)

numVert = mm.eval('polyEvaluate -v')

print 'const vec3 '+str(VERT_OUTPUT_NAME)+'[' + str(numVert[0]) + '] = vec3[' + str(numVert[0]) + ']('

for v in range(numVert[0]):
    vert = mm.eval('pointPosition' + ' ' + str(selection[0]) + '.vtx[' + str(v) + ']')
    if v < numVert[0] -1:
        print 'vec3(', vert[0], ', ', vert[1], ', ',vert[2],'), '
    else:
        print 'vec3(', vert[0], ', ', vert[1], ', ',vert[2],') '
print ');'    
    
numFace = mm.eval('polyEvaluate -t')

print 'const ivec3 '+str(INDEX_OUTPUT_NAME)+'['+str(numFace[0])+'] = ivec3['+str(numFace[0])+']('  

for f in range(numFace[0]):
    face = mm.eval('polyInfo -faceToVertex' + ' ' +  str(selection[0]) + '.f[' + str(f) + ']')
    ind =  face[0].split()
    if f < numFace[0] -1:
        print 'ivec3(', ind[2], ', ', ind[3], ', ', ind[4],'), '
    else:
        print 'ivec3(', ind[2], ', ', ind[3], ', ', ind[4],') '
print ');'