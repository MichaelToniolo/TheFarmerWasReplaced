pos = 0
import PLANTA
while True:
	for i in range(8):

#POSX 0 ARVRE + GIRAS
		if get_pos_x() == 0:
			if pos % 2 == 0:
				plant(Entities.Tree)
			else:
				PLANTA.Giras()
		if can_harvest():
				harvest()
#POSX 1 ZENAS
		if get_pos_x() == 1:
			PLANTA.Giras()
#POSX 2 E 5
		if (get_pos_x() == 2 or get_pos_x() == 3):
			PLANTA.Zenas()
#POSX 4 POSY 3
		if get_pos_x() == 4 or get_pos_x() == 5 or get_pos_x() == 6 or get_pos_x() == 7:
			PLANTA.Abras()
		move(North)
		pos += 1
	move(East)
