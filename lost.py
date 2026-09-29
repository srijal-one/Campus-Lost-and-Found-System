def report_lost(lost_items):
	print("\n------Report Lost Item--------")
	
	name = input("Enter Item Name :  ")
	place = input("Where did you lose it?  :  ")
	item = [name , place , "Lost"]
	
	lost_items.append(item)
	
	print("Lost Item Added Successfully.")
	
	
def view_lost(lost_items):
	print("\n-------Lost Items-------")
	
	if len(lost_items) == 0:
		print("No Lost Items . ")
	else:
		for item in lost_items:
			print("Item : " , item[0])
			print("Place :" , item[1])
			print("Status : " , item[2])
			print()	
	