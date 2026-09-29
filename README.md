# Campus Lost and Found System 
A simple Python CLI program system which help us to keep the track of lost and found items around the college campus.

# Project Description 
Suppose if you lose your Mobile Phone in campus, possible ways to find that keep check on notice boards, asks on the group chats or just wait for the time when someone will found the phone, they will come and give it you. Nothing works properly and it is very difficult to manage all these in the busy schedules of college. Here Campus Lost and Found gives us a simple system. Students can report what they have lost or found in the campus or can search for items as well. Once the item claimed by the owner, we can also change the status of the items. We can even delete wrong or duplicate entries from it, if needed.

# Who is it for? (Target Users)
Students who lost or found something in the campus or the campus staff members or in-desk person who keep tracks on these items and maintain the records by the time.

# Features
1. You can report a lost item or found item with its name and place.
2. View all the lost and found items at once separately in their respective menus.
3. Search for any item across lost and found items list.
4. Change the item status to "Returned" if handover to its owner.
5. Delete incorrect or duplicate entries from the system.
6. Simple numbered menu for easy navigation of features and invalid option choosen message if choice selection is wrong.

Build by using Python - 3 with only use of standard library. There are no external packages and you can run the program in terminal with no GUI or browser.

# Setup and Installation
1. Install Python. On Windows, download it from python.org/downloads and tick "Add Python to PATH" during installation. For macOs or Linux, it usually installed already and you can check it by running python3 --version in a terminal.
2. Download the repository as a ZIP file, extract it and open the terminal inside that folder.
3. Install dependencies. None are needed and there is no requirements file and no pip install step.
4. No Configuration is needed. There are no environment variables or config files.
5. Now run the project using main.py file in the terminal.

You will now get a numbered menu. Type a number and then press Enter key for the action and You can exit the program by choosing 9.

# How Will Menu Work?
1. Option 1 will report the Lost item and Option 2 will report the Found item.
2. Option 3 and Option 4 will show the added items in both lost and found items list.
3. Option 5 will Search for any item and Option 6 will will mark the item as returned when you enter the item's name and place.
4. Option 7 and Option 8 works for deleting the lost and found items respectively.
5. Option 9 will exits the program when you choose it.

# Testing
The project is tested manually through the terminal by taking different possible inputs:
1. Report a lost or found item and then viewing them from menu options confirms that they are added.
2. Search for the item that exists in the system and for one that does not exist in it.
3. After Marking status of an item to returned and again check it's status to confirm.
4. Reporting same item in both lost and found and check after marking returned it updates in both lists or not.
5. Delete the items from list and again view the lists.
6. Entering a invalid menu number to confirm it shows error message instead of crashing system.

# Project Structure
1. main.py - Main file and program flow
2. lost.py - for reporting and viewing lost items
3. found.py - for reporting and viewing founded items
4. search.py - to search for items in the two ists
5. returned.py - for marking returned item
6. delete.py - to delete any lost or found item

# Future Enhancements
I have plan to include saving data to a file so that recorded entries will remain in the system and doesn't vanish when we close the programm. Adding Unique IDs to items so that we don't have to depend only on name and place, suggesting matches between lost and found items, SQLite storage and addition of GUI.

