pos = 0
while True:
	for i in range(6):
#VERIFICA POSX E PLANTAR ZENOURAS NA POSX 1 E 3
		if get_pos_x() == 1 or get_pos_x() == 3:
			if can_harvest():
				harvest()
			till()
			plant(Entities.Carrot)
			if get_water() <= 1 and num_items(Items.Water) > 40 and get_entity_type() == Entities.Carrot:
				use_item(Items.Water)
#PLANTANDO MADEIRA NA POSX 0 E 2 COM ARVORE
		if get_pos_x() == 0 or get_pos_x() == 2:
			if pos % 2 == 0:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
		if can_harvest():
				harvest()
#PLANTANDO GIRAS NAS POSX 4 E 5
		if (get_pos_x() == 4 or get_pos_x() == 5) and (get_pos_y() == 2 or get_pos_y() == 3 or get_pos_y() == 4 or get_pos_y() == 5):
			till()
			plant(Entities.Sunflower)
			if get_water() <= 1 and num_items(Items.Water) > 40 and get_entity_type() == Entities.Sunflower:
				use_item(Items.Water)
		if can_harvest():
			harvest()
#PLANTANDO ABOBRA NAS POSX 4 POSY 3
		if (get_pos_x() == 4 or get_pos_x() == 5) and (get_pos_y() == 0 or get_pos_y() == 1):
			till()
			plant(Entities.Pumpkin)
			if get_water() <= 1 and num_items(Items.Water) > 20 and get_entity_type() == Entities.Pumpkin:
				use_item(Items.Water)
		if can_harvest():
			harvest()
		move(North)
		pos += 1
	move(East)
