import csv
import pandas

menuOptions = ["New Ticket", "Current Tickets", "View Ticket", "Exit"]
ticketMenuOptions = ["Update Ticket", "Close Ticket", "Return to Main Menu"]
currentTickets = []
ticketNumbers = []
print("Welcome to PyTicketing!\n")

sheet = open('tickets.csv')
csvreader = csv.reader(sheet)
ticketSheet = pandas.read_csv("tickets.csv")




# New ticket function
# Allows for entry of a new ticket into a csv file
# Next steps: add records to a DB
def newTicket(number, discription, enteredBy):
    newTicketList = [number, discription, enteredBy, 'New']
    with open('tickets.csv', 'a') as sheet:
        writer_object = csv.writer(sheet)
        writer_object.writerow(newTicketList)
        sheet.close()

# Read current ticket status function
# Indexing is done on a 0 start posistion, however ticket numbers have a 1 start position
def getTicketStatus(number):
    for i in range(len(ticketSheet.Number)):
        if int(ticketSheet.Number[i]) == int(number):
            print("Ticket status: " + str(ticketSheet.Status[i]) + "\n")

# Print a ticket function
def printTicket(number):
    for i in range(len(ticketSheet.Number)):
        if int(ticketSheet.Number[i]) == int(number):
            print("Ticket number: " + str(ticketSheet.Number[i]))
            print("Ticket discription: " + str(ticketSheet.Discription[i]))
            print("Ticket status: " + str(ticketSheet.Status[i]))
            print("Ticket entered by: " + str(ticketSheet.EnteredBy[i]) + "\n")

# Set ticket status function
# Indexing is done on a 0 start posistion, however ticket numbers have a 1 start position
def setTicketStatus(number, status):
        for i in range(len(ticketSheet.Number)):
            if int(ticketSheet.Number[i]) == int(number):
                ticketSheet.Status[i] = status
                ticketSheet.to_csv('tickets.csv', index=False)
                print("Ticket status updated to: " + str(status) + "\n")

# Add notes and other information to a ticket discription
def updateTicket(number):
    for i in range(len(ticketSheet.Number)):
        if int(ticketSheet.Number[i]) == int(number):
            print("Ticket discription: " + str(ticketSheet.Discription[i]) + "\n")
            newDiscription = input("Enter new note: ")
            ticketSheet.Discription[i] = newDiscription
            ticketSheet.to_csv('tickets.csv', index=False)
            print("Ticket discription updated to: " + str(newDiscription) + "\n")

# Close a ticket
def closeTicket(number):
    for i in range(len(ticketSheet.Number)):
        if int(ticketSheet.Number[i]) == int(number):
            ticketSheet.Status[i] = 'Closed'
            ticketSheet.to_csv('tickets.csv', index=False)
            print("Ticket number " + str(number) + " status updated to: Closed\n")


# Main application loop
while True:
    for i in range(len(menuOptions)):
        print(str(i + 1) + ".) " + str(menuOptions[i]))
    print('\n') # Spacer
    userChoice = input().lower()
    exitOption = len(menuOptions)

    # Exit option
    if userChoice == "exit" or userChoice == str(exitOption):
        break

    # Create new ticket
    elif userChoice == 'new ticket' or userChoice == str(1):
        newTicNumber = input("Enter ticket number: ")
        newTicDiscrption = input("Enter a ticket discription: ")
        newTicSubmitter = input("Enter the submitter: ")
        newTicket(newTicNumber, newTicDiscrption, newTicSubmitter)
    
    # List current tickets
    elif userChoice == "current tickets" or userChoice == str(2):
        print('\n') # Spacer
        print(ticketSheet)
        print('\n') # Spacer

    # View ticket and ticket sub menu
    elif userChoice == "View ticket" or userChoice == str(3):
        while True:
            viewTicketNumber = int(input("Enter ticket number: "))
            printTicket(viewTicketNumber)
            for i in range(len(ticketMenuOptions)):
                print(str(i + 1) + ".) " + str(ticketMenuOptions[i]))
            exitOption = len(ticketMenuOptions)
            subUserChoice = input().lower()
            print("Made it to sub menu choices")
            # Back to main menu
            if subUserChoice == "Return to Main Menu" or userChoice == str(exitOption):
                break
            # Update ticket discription
            elif subUserChoice == "update ticket discription" or userChoice == str(1):
                updateTicket(viewTicketNumber)
                setTicketStatus(viewTicketNumber, 'Open')
            # Close ticket
            elif subUserChoice == "close ticket" or userChoice == str(2):
                print('Are you sure? (Y/N)')
                closeTicUserChoice = input()
                if userChoice == 'Y':
                    closeTicket(viewTicketNumber)
        