from lost import report_lost , view_lost
from found import report_found , view_found
from search import search_item
from returned import marked_returned
from delete import delete_lost , delete_found

lost_items = []
found_items = []

while True:
	
	print("---------------------------------------------------\n      CAMPUS LOST AND FOUND MANAGEMENT\n---------------------------------------------------\n")
	print("1.Report Lost Item")
	print("2. Report Found Item")
	print("3. View Lost Items")
	print("4. View Found Items")
	print("5. Search Items")
	print("6. Mark Item As Returned")
	print("7. Delete lost Item")
	print("8. Delete Found Item")
	print("9. Exit")
	
	choice = input("\nEnter your Choice : ")
	if choice == "1":
		report_lost(lost_items)
		
	elif choice == "2":
		report_found(found_items)
		
	elif choice == "3":
		view_lost(lost_items)
		
	elif choice == "4":
		view_found(found_items)
		
	elif choice == "5":
		search_item(lost_items , found_items)
		
	elif choice =="6":
		marked_returned(lost_items, found_items)
		
	elif choice == "7":
		delete_lost(lost_items)
		
	elif choice =="8":
		delete_found(found_items)
		
	elif choice =="9":
		print("Program Ended . Thank You!!!")
		break
		
	else:
		print("Invalid Choice Entered")