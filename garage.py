import random

class Garage():

    def __init__ (self):
        self.tickets = list(range(1,6))
        self.parking_spaces = list(range(1,6))
        self.current_tickets = {}
        self.ticket_num = None
        self.parking_space = None

    def takeTicket(self):
        while True:
            entrance = input("Would you like to take a ticket? Y/N: ")
            if entrance.lower().strip() == 'y' and self.tickets:
                self.ticket_num = self.tickets.pop()
                self.parking_space = self.parking_spaces.pop()
                self.current_tickets['Paid'] = False
                print("\nHere is your parking ticket!")
                print("...You better not leave before you pay....")
                break
            elif entrance.lower().strip() == 'y' and not self.tickets:
                print("\nSorry! The parking garage is currently full.")
                break
            elif entrance.lower().strip() == 'n':
                print("Ok never mind... Have a nice day!")
                break
            else:
                print("Invalid option. Please enter a valid choice.")

    def payForParking(self):
        ticket_price = random.randint(1,50)
        while True:
            parking_payment = int(input(f"\nThe parking ticket costs ${ticket_price}. Please enter that amount. "))
            if parking_payment == ticket_price:
                print("\nThank you! Your ticket has been paid.")
                print("You have 15 minutes to leave the garage.")
                self.current_tickets['Paid'] = True
                break
            elif parking_payment < ticket_price:
                print(f"You paid ${parking_payment}. You still owe ${ticket_price-parking_payment}.")
                ticket_price = ticket_price-parking_payment
            elif parking_payment > ticket_price:
                print(f"You paid too much! Here is ${parking_payment-ticket_price} back! Thank you!")
                print("You have 15 minutes to leave the garage.")
                break
            else:
                print("Please enter a valid amount.")

    def leaveGarage(self):
        while True:
            if self.current_tickets['Paid'] == True:
                print("Thank you for paying. Have a nice day!")
                self.tickets.append(self.ticket_num)
                self.parking_spaces.append(self.parking_space)
                break
            else:
                self.payForParking()    

parking_garage = Garage()

def run():
    while True:
        print("""
            Welcome to Coding Temple's Garage! Here are the following options:
            [1] Take Ticket
            [2] Pay for Parking
            [3] Leave Garage
            [4] Quit
        """)
        response = input("What would you like to do? ")
        if response.lower().strip() == '1':
            parking_garage.takeTicket()
        elif response.lower().strip() == '2':
            parking_garage.payForParking()
        elif response.lower().strip() == '3':
            parking_garage.leaveGarage()
            break
        elif response.lower().strip() == '4':
            print("If you haven't paid for your ticket yet, please do so by selecting option 2. Thank you!")
            break
        else:
            print("Please enter a valid option.")

run()