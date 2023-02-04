"""
Name: Drew Cochran
# Date: 01FEB2023
# Description: Program that creates and stores a table of household items, by name and value, that continually runs
until the user presses the correct option to exit the program. The program will also display all of the data the user
has entered into the table if the correct option is selected. Once the closing option is selected, the program writes
the data to a txt file and stops the program.
Changelog:
01FEB2023: Created file, description, began coding While loop and menu
01FEB2023: Ended up coding all the way through. Added While loop under option 1 to allow user to continue inputting
            items indefinitely until 'main' is typed, taking user back to main menu. Also created function to call the
            menu of options when needed.
04FEB2023: No change; opened code to run program to demonstrate 2nd while loop in option 1

"""

# Initial Variable setup
strItemName = ''
strItemValue = ''
strUserChoice = ''
lstRow = []
lstTable = []

# function to print the menu


def menu_of_options():
    # Print menu of options
    print("""
    Menu of Options
    1) Add Data to List
    2) Display Current Data
    3) Exit and Save to File
    """)

# While loop to keep running until Option 3 is selected


while(True):
    # Call MenuOfOptions function to display menu
    menu_of_options()

    # Input to strUserChoice to determine next steps
    strUserChoice = input("Which option would you like to perform? Type exit to end program (1 to 3): ")

    # If elif and else statements to determine actions upon user choice
    # Option 1 If
    if strUserChoice == '1':
        print("Type in a 'Name' and Value for your Household Items. Type 'main' and hit enter to go to main menu.")
        while(True):
            # Entering items continuously
            strItemName = input("Enter a Name: ")

            # If check for user who made an error in selection
            if strItemName.lower() == 'main':
                break

            strItemValue = input("Enter a Value: ")

            # If check if user wants to leave before item is completely entered.
            if strItemValue.lower() == 'main':
                break
            lstRow = [strItemName, strItemValue]
            lstTable += [lstRow]

    # Option 2 elif
    elif strUserChoice == '2':
        print("Your Current Data is: ")
        for row in lstTable:
            print('' + row[0] + ', ' + row[1])

    # Option 3 elif
    elif strUserChoice == '3':
        objFile = open("HomeInventory.txt", "a")
        for row in lstTable:
            objFile.write(str(row[0] + ", " + str(row[1] + "\n")))
        objFile.close()
        print("Data was saved to current directory titled HomeInventory.txt. Congratulations!")
        break

    # Option exit elif
    elif strUserChoice.lower() == 'exit':
        exit()

    # Option if user enters anything other than 1, 2 or 3
    else:
        print("Please choose only 1, 2, or 3. Type exit to end program.")

# Prints data user entered
print("Your newest inputted Data is: ")
for row in lstTable:
    print('' + row[0] + ', ' + row[1])
print("Done!")