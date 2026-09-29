def delete_lost(lost_items):
	print("\n------Delete Lost Items-------")
	
	if len(lost_items) == 0:
		print("No lost items to Delete.")
		return
		
	name = input("Enter Item name to delete : ")
	place = input("Enter place : ")
	for item in lost_items:
		if item[0].lower() == name.lower() and item[1].lower() == place.lower():
			lost_items.remove(item)
			print("Item Deleted Successfully.")
			return
				
	print("Item not Found.")
		
		
def delete_found(found_items):
		print("\n----- Delete Found Items------")
		
		if len(found_items) == 0:
			print("No found items to Delete.")
			return
			
		name = input("Enter Item name to delete : ")
		place = input("Enter place : ")
		for item in found_items:
			if item[0].lower() == name.lower() and item[1].lower() == place.lower():
				found_items.remove(item)
				print("Item Deleted Successfully.")
				return
					
		print("Item not Found.")
		
		
			