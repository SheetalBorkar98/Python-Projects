
class Train:

    seatno = 0

    def __init__(self, name, seat, fare, t_seat):
        self.name = name
        self.seat = seat
        self.fare = fare
        self.t_seat = t_seat

    def bookTicket(self):
        if len(self.seat) > 0:
            print(f"\nSeat number {self.seat.pop()} is booked for you..")
        else:
            print("\nSeats Unavailable..")

    def getStatus(self):
        print("\nTrain name : ",self.name)
        if len(self.seat) == 0:
            print("Seats Unavailable.")
        else:
            print("\nNumber of Seats available : ",len(self.seat))
            print("\nAvailable seat number : ",self.seat)

    def getFareInfo(self):
        print("\nTrain fare : ",self.fare)

    def cancelTicket(self):
        if self.seatno not in self.t_seat:
            print("\nInvalid seat number (Seat not available in train)..")
        elif self.seatno not in self.seat:
            self.seat.add(self.seatno)
            print(f"\nSeat number {self.seatno} is available now..")
            print("\nAvailable seats number : ",self.seat)
        elif self.seatno in self.seat:
            print("\nSeat was not already booked..Please enter valid booked seat number to cancel the ticket.")

# seats written in tuple to compare so that original seats cannot be changed.
t_seat = (1, 2, 3, 4, 5)

# seats written in set to perform operation (add and remove) and avoid repeated numbers.
seat = {1, 2, 3, 4, 5}

# Initializing the train
t1 = Train("GaribRath Express", seat, 500, t_seat)

train = True


while train:
    try:
        print('''
        Choose from the following options :
        1) Get Status of the Train
        2) Get Fare information of train
        3) Book Tickets
        4) Cancel Ticket
        5) Quit
        ''')

        user = int(input("Enter your choice : "))
        if user == 1:
            t1.getStatus()
        elif user == 2:
            t1.getFareInfo()
        elif user == 3:
            t1.bookTicket()
        elif user == 4:
            a = int(input("\nEnter seat number to cancel : "))
            t1.seatno = a
            t1.cancelTicket()
        elif user == 5:
            train = False
        else:
            print("\nEnter Valid Choice !!")

    except Exception as e:
        print("Please enter a valid choice..")

print("\nThank you !! Visit again..\n")
