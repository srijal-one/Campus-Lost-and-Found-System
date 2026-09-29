def report_found(found_items):
	print("\n-------Report Found Item------")
	
	name = input("Enter item name : ")
	place = input("Where did you find it?  : ")
	item = [name , place , "Found"]
	
	found_items.append(item)
	print("Found Item Added Successfully.")
	
	
	
def view_found(found_items):
	print("\n-------Found Items------")
	
	if len(found_items) == 0:
		print("No Found Items. ")
	else:
		for item in found_items:
			print("Item : " , item[0])
			print("Place : " , item[1])
			print("Status : " , item[2])
			print()