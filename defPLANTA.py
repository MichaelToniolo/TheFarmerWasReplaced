#PLANTAGIRAS
def Giras():
	till()
	plant(Entities.Sunflower)
	if get_water() <= 1 and num_items(Items.Water) > 200 and get_entity_type() == Entities.Sunflower:
		use_item(Items.Water)
	if can_harvest():
		harvest()

#PLNATAABRAS
def Abras():
	if get_ground_type() != Grounds.Soil:
			till()
			plant(Entities.Pumpkin)
			if get_water() <= 1 and num_items(Items.Water) > 200 and get_entity_type() == Entities.Pumpkin:
				use_item(Items.Water)
	elif can_harvest() == False:
		plant(Entities.Pumpkin)
	else:
		harvest()
			
		
#PLANTAZENAS
def Zenas():
	if can_harvest():
		harvest()
	till()
	plant(Entities.Carrot)
	if get_water() <= 1 and num_items(Items.Water) > 200 and get_entity_type() == Entities.Carrot:
		use_item(Items.Water)
	
