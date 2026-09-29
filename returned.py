def marked_returned(lost_items , found_items):
	print("\n-------- Mark Item as Returned-------")
	
	name = input("Enter Item Name : ")
	place = input("Enter place : ")
	
	matched = False
	
	for item in lost_items:
		if item[0].lower() == name.lower() and item[1].lower() == place.lower():
			item[2] = "Returned"
			matched = True
			
			
			
			
	for item in found_items:
		if item[0].lower() == name.lower() and item[1].lower() == place.lower():
			item[2] = "Returned"
			matched = True
			
	if matched:
		print("Item Marked as Returned.")
	else:
			print("Item not Found.")
			
			