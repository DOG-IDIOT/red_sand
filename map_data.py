############################################
##                                        ##
##   '||    ||'                           ##
##    |||  |||   ....   ... ...   ....    ##
##    |'|..'||  '' .||   ||'  || ||. '    ##
##    | '|' ||  .|' ||   ||    | . '|..   ##
##   .|. | .||. '|..'|'  ||...'  |'..|'   ##
##                       ||               ##
##                      ''''              ##
##                                        ##
##                                        ##
##	Data structure for maps is:           ##
##	map_name = [z-layer[row[tile]]]       ##
##                                        ##
##  Possible tiles:                       ##
##	None 	= Empty space                 ##
##	0 		= Grey smooth stone           ##
##	1 		= Grey bricks                 ##
##	2		= Green smooth stone          ##
##	3		= Grey smooth stone, shadow   ##
##                                        ##
##                                        ##
############################################


# # # # # # # # 
#             #
# Testing map #
#             #
# # # # # # # # 

map_1 = [

	## Ground
	## Determines size of map; don't put blocks here!
	[
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
	], 
	
	## 1
	[
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	], 
	
	## 2
	[
		[0, 0, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0]
	], 
	
	## 3
	[
		[0, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0]
	],
	
		## 4
	[
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
		[0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0]
	]
	
]		
