pos = 0
import PLANTA, DEFS_TEST
while True:
	for i in range(6):
#POSX 1 E 3
		if get_pos_x() == 1:
			PLANTA.Zenas()
#POSX 0 E 2
		if get_pos_x() == 0:
			if pos % 2 == 0:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
		if can_harvest():
				harvest()
#POSX 4 E 5
		if (get_pos_x() == 4 or get_pos_x() == 5) and (get_pos_y() == 2 or get_pos_y() == 3 or get_pos_y() == 4 or get_pos_y() == 5):
			PLANTA.Giras()
#POSX 4 POSY 3
		if (get_pos_x() == 4 or get_pos_x() == 5) and (get_pos_y() == 0 or get_pos_y() == 1):

			PLANTA.Abras()
		if get_pos_x() == 2 or get_pos_x() == 3:
			PLANTA.Abras()
		move(North)
		pos += 1
	move(East)
