class ParkingGarage:
    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        if self.tickets:
           ticket = self.tickets.pop(0)
           self.parkingSpaces.pop(0)
           self.currentTicket = {"ticket_number": ticket, "paid": False}
           print("Ticket taken. Parking space allocated.")

    def payForParking(self):
        if not self.currentTicket:
            print("Please take a ticket first.")
            return

        amount = input("Enter payment amount: ")
        if amount:
            print("Payment received. You have 15 minutes to leave.")
            self.currentTicket["paid"] = True

    def leaveGarage(self):
        if not self.currentTicket:
            print("Please take a ticket first.")
            return

        if self.currentTicket["paid"]:
            print("Thank you, have a nice day!")
            self.parkingSpaces.append(1)
            self.tickets.append(1)
            self.currentTicket = None
        else:
            self.payForParking()

# Instantiate the ParkingGarage class
tickets = [1, 2, 3, 4, 5]  # Example ticket numbers
parkingSpaces = [1, 1, 1, 1, 1]  # Example parking spaces availability
currentTicket = None  # Initially no ticket issued

garage = ParkingGarage(tickets, parkingSpaces, currentTicket)

# Main loop
while True:
    action = input("What would you like to do? (take/pay/leave/quit): ")
    if action == "take":
        garage.takeTicket()
    elif action == "pay":
        garage.payForParking()
    elif action == "leave":
        garage.leaveGarage()
    elif action == "quit":
        print("Exiting program.")
        break
    else:
        print("Invalid input. Please try again.")