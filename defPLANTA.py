#PLANTAGIRAS
def Giras():
	till()
	plant(Entities.Sunflower)
	if get_water() <= 1 and num_items(Items.Water) > 20 and get_entity_type() == Entities.Sunflower:
		use_item(Items.Water)
	if can_harvest():
		harvest()

#PLNTAABRAS
def Abras():
	till()
	plant(Entities.Pumpkin)
	if get_water() <= 1 and num_items(Items.Water) > 20 and get_entity_type() == Entities.Pumpkin:
		use_item(Items.Water)

	if can_harvest():
		harvest()
#PLANTAZENAS
def Zenas():
	if can_harvest():
		harvest()
	till()
	plant(Entities.Carrot)
	if get_water() <= 1 and num_items(Items.Water) > 240 and get_entity_type() == Entities.Carrot:
		use_item(Items.Water)
	
