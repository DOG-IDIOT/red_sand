####################################################
##                                                ##
##      |                             .           ##
##     |||     ....   ....    ....  .||.   ....   ##
##    |  ||   ||. '  ||. '  .|...||  ||   ||. '   ##
##   .''''|.  . '|.. . '|.. ||       ||   . '|..  ##
##  .|.  .||. |'..|' |'..|'  '|...'  '|.' |'..|'  ##
##                                                ##
##                                                ##
####################################################


import constants as C
import pygame
pygame.init()


# 
# '||''''|                    .          
#  ||  .     ...   .. ...   .||.   ....  
#  ||''|   .|  '|.  ||  ||   ||   ||. '  
#  ||      ||   ||  ||  ||   ||   . '|.. 
# .||.      '|..|' .||. ||.  '|.' |'..|' 
#                                        


DEBUG_FONT = pygame.font.Font("assets/manaspc.ttf",16)


# 
# |''||''|  ||  '||                 
#    ||    ...   ||    ....   ....  
#    ||     ||   ||  .|...|| ||. '  
#    ||     ||   ||  ||      . '|.. 
#   .||.   .||. .||.  '|...' |'..|' 
#                                   
#       


u_red_sand		= pygame.image.load('assets/red_sand.png')
red_sand		= pygame.transform.scale(u_red_sand, (C.TILE_WIDTH*2, C.TILE_HEIGHT*2)) 

u_red_sand2		= pygame.image.load('assets/red_sand2.png')
red_sand2		= pygame.transform.scale(u_red_sand2, (C.TILE_WIDTH*2, C.TILE_HEIGHT*2)) 

u_floor			= pygame.image.load('assets/floor.png')
floor			= pygame.transform.scale(u_floor, (C.TILE_WIDTH*2, C.TILE_HEIGHT*2)) 

u_wall			= pygame.image.load('assets/wall.png')
wall			= pygame.transform.scale(u_wall, (C.TILE_WIDTH*2, C.TILE_HEIGHT*2)) 

u_grass			= pygame.image.load('assets/grass.png')
grass			= pygame.transform.scale(u_grass, (C.TILE_WIDTH*2, C.TILE_HEIGHT*2)) 

u_unexplored	= pygame.image.load('assets/floor_unexplored.png')
unexplored		= pygame.transform.scale(u_unexplored, (C.TILE_WIDTH*2, C.TILE_HEIGHT*2)) 

u_floor_shadow 	= pygame.image.load('assets/floor_shadow.png')
floor_shadow	= pygame.transform.scale(u_floor_shadow, (C.TILE_WIDTH*2, C.TILE_HEIGHT*2)) 


# 
#  .|'''.|                    ||    .                  
#  ||..  '  ... ...  ... ..  ...  .||.    ....   ....  
#   ''|||.   ||'  ||  ||' ''  ||   ||   .|...|| ||. '  
# .     '||  ||    |  ||      ||   ||   ||      . '|.. 
# |'....|'   ||...'  .||.    .||.  '|.'  '|...' |'..|' 
#            ||                                        
#           '''' 


u_char_1		= pygame.image.load('assets/char_1.png')
char_1			= pygame.transform.scale(u_char_1, (C.TILE_WIDTH, C.TILE_HEIGHT)) 

u_shadow_small	= pygame.image.load('assets/shadow_small.png')
shadow_small	= pygame.transform.scale(u_shadow_small, (C.TILE_WIDTH, C.TILE_HEIGHT)) 


# 
# '||'                                           
#  ||  .. .. ..    ....     ... .   ....   ....  
#  ||   || || ||  '' .||   || ||  .|...|| ||. '  
#  ||   || || ||  .|' ||    |''   ||      . '|.. 
# .||. .|| || ||. '|..'|'  '||||.  '|...' |'..|' 
#                         .|....'                
#                                          


u_bg_1		= pygame.image.load('assets/bg_1.png')
bg_1		= pygame.transform.scale(u_bg_1, (C.MAP_W, C.MAP_H))