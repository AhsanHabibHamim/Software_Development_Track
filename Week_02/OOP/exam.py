class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False

class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        return False

class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []
        self.admin = Admin("admin", "1234")

    def add_bus(self, bus):
        self.buses.append(bus)

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def show_buses(self):
        for bus in self.buses:
            print(f"Bus Number: {bus.number}, Route: {bus.route}, Available Seats: {bus.available_seats()}")

    def book_ticket(self, bus_number, name, phone):
        bus = None
        for b in self.buses:
            if b.number == bus_number:
                bus = b
                break
        if bus and bus.book_seat():
            passenger = Passenger(name, phone, bus)
            self.add_passenger(passenger)
            print(f"Ticket booked successfully for {name} on Bus {bus_number}. Fare: ৳500")
        else:
            print("No available seats on this bus.")

    def admin_login(self):
        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")
        if self.admin.login(username, password):
            print("Login Successful!")
            return True
        else:
            print("Invalid credentials. Please try again.")
            return False

    def user_menu(self):
        while True:
            print("\nMenu:")
            print("1. Admin Login")
            print("2. Book Ticket")
            print("3. View Buses")
            print("4. Exit")
            
            choice = input("Enter your choice: ")

            if choice == '1':
                if self.admin_login():
                    self.admin_menu()
            elif choice == '2':
                bus_number = input("Enter Bus Number: ")
                name = input("Enter Passenger Name: ")
                phone = input("Enter Passenger Phone: ")
                self.book_ticket(bus_number, name, phone)
            elif choice == '3':
                self.show_buses()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Add Bus")
            print("2. View All Buses")
            print("3. Logout")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                number = input("Enter Bus Number: ")
                route = input("Enter Bus Route: ")
                seats = int(input("Enter Total Seats: "))
                bus = Bus(number, route, seats)
                self.add_bus(bus)
                print(f"Bus {number} added to the system!")
            elif choice == '2':
                self.show_buses()
            elif choice == '3':
                print("Logged out!")
                break
            else:
                print("Invalid choice. Please try again.")

# Main Code to run the system
if __name__ == "__main__":
    system = BusSystem()

    while True:
        system.user_menu()