import csv
# import pandas

menuOptions = ["New Ticket", "Current Tickets", "Update Ticket", "Exit"]
currentTickets = []
print("Welcome to PyTicketing!\n")

sheet = open('tickets.csv')
csvreader = csv.reader(sheet)


# New ticket function
# Allows for entry of a new ticket into a csv file
# Next steps: add records to a DB
def newTicket(number, discription, enteredBy):
    newTicketList = [number, discription, enteredBy, 'New']
    with open('tickets.csv', 'a') as sheet:
        writer_object = csv.writer(sheet)
        writer_object.writerow(newTicketList)
        sheet.close()

# def getTicketStatus(number):

# def setTicketStatus(number):

# def updateTicket(number):



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
        for row in csvreader:
            currentTickets.append(row)
        for i in range(len(currentTickets)):
            print(str(currentTickets[i]))
        print('\n') # Spacer

    #Update ticket
    elif userChoice == "update ticket" or userChoice == str(3):
        print("HEY BEN YOU NEED TO ADD THIS")