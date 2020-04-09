############################################################################
##                                                                        ##
##                                                                        ##
##   ..|'''.|                           .                      .          ##
## .|'     '    ...   .. ...    ....  .||.   ....   .. ...   .||.   ....  ##
## ||         .|  '|.  ||  ||  ||. '   ||   '' .||   ||  ||   ||   ||. '  ##
## '|.      . ||   ||  ||  ||  . '|..  ||   .|' ||   ||  ||   ||   . '|.. ##
##  ''|....'   '|..|' .||. ||. |'..|'  '|.' '|..'|' .||. ||.  '|.' |'..|' ##
##                                                                        ##
##                                                                        ##
############################################################################

# # #  DO NOT TOUCH # # #
import pygame           #
pygame.init()           #
# # # # # # # # # # # # #
 

## Render settings #########################################################

# Maximum FPS
FPS_TARGET = 33

# Scale factor for assets
# Can be a float, but scaling will look weird
ZOOM = 2

# Main window dimensions in px
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 700

# Tile dimensions in px
TILE_HEIGHT = int(32 * ZOOM)
TILE_WIDTH = int(32 * ZOOM)

# Map dimensions in px
# !!! Background asset should match this !!!
MAP_H = int(1500 * ZOOM)
MAP_W = int(1500 * ZOOM)

# Distance (in tiles) up to which tiles are rendered
RENDER_SIZE = 22 // ZOOM

## Camera settings #########################################################

# Viewport dimensions in px
# Should match main window dimensions
CAMERA_HEIGHT = 700
CAMERA_WIDTH = 700

# Tracking speed of the camera, from 0.01 - 1
TRACKING_SPEED = 0.2


## Input settings ##########################################################
 
# Time in ms before a held key retriggers (default = 340)
KEY_REPEAT_THRESH = 340

# Time in ms before it retriggers after that (default = 100)
KEY_REPEAT_SPEED = 100