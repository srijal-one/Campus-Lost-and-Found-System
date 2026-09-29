def search_item(lost_items , found_items):
	print("\n------Search Items-------")
	
	name = input("Enter Item Name : ")
	
	found = False
	
	for item in lost_items:
		if item[0].lower() == name.lower():
			print("Item : " , item[0])
			print("Place : " , item[1])
			print("Status : " , item[2])
			print()
			found = True
			
	for item in found_items:
		if item[0].lower() == name.lower():
			print("Item : " , item[0])
			print("Place : " , item[1])
			print("Status : " , item[2])
			print()
			found = True
			
	if found == False:
		print("Item Not Found.")