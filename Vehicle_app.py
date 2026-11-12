# Vehicle_app.py
# Name: Stephanie Garcia Garcia
# Date: 11/11/2026

# ---------- Classes ------------

# Superclass
class Vehicle:

    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):

    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self. roof = roof

    def display(self):
        #print attribute
        print("\nHere is your vehicle's information:")
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")


def ask_text(prompt):
    
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")


def ask_year(prompt):

    while True:
        value = input(prompt).strip()
        if value.isdigit() and 1886 <= int(value) <= 2100:
            return int(value)
        print("Please enter a valid 4-digit year (for example, 2022).")


def ask_doors(prompt):

    while True:
        value = input(prompt).strip()
        if value in ("2", "4"):
            return int(value)
        print("Please enter 2 or 4.")


def ask_roof(prompt):

    while True:
        value = input(prompt).strip().lower().replace("-", " ")
        if value in("solid", "solid roof"):
            return "solid"
        if value in("sun roof", "sunroof"):
            return "sun roof"
        print("Please enter 'solid' or 'sun roof'.")


def main():
    print("Let's enter the details for your car.\n")
 
    year = ask_year("Year (e.g., 2022): ")
    make = ask_text("Make (e.g., Toyota): ")
    model = ask_text("Model (e.g., Corolla): ")
    doors = ask_doors("Number of doors (2 or 4): ")
    roof = ask_roof("Type of roof (solid or sun roof): ")
 
    # The app stores "car" as the vehicle type in the Vehicle super class.
    car = Automobile("car", year, make, model, doors, roof)
    car.display()
 
 
if __name__ == "__main__":
    main()
 