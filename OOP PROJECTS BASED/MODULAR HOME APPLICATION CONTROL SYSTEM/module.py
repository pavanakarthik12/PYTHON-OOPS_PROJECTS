class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print(f"{self.name} is switched ON!")
    
    def turn_off(self):
        self.is_on = False
        print(f"{self.name} is switched OFF!")
    
    def get_status(self):
        return f"{self.name} is {'ON' if self.is_on else 'OFF'}"


class Light(Device):
    def __init__(self, name):
        super().__init__(name)
        self.brightness = 50  # Default brightness
    
    def set_brightness(self):
        level = int(input("SET brightness level (0-100): "))
        if 0 <= level <= 100:
            self.brightness = level
            print(f"{self.name} brightness set to {self.brightness}%")
        else:
            print("Invalid brightness level! Use values between 0-100.")
    
    def get_status(self):
        return f"{self.name}: {'ON' if self.is_on else 'OFF'}, Brightness: {self.brightness}%"


class Fan(Device):
    def __init__(self, name):
        super().__init__(name)
        self.fanspeed = 1  # Default speed
    
    def set_fan_speed(self):
        level = int(input("Set fan speed (1-5): "))
        if 1 <= level <= 5:
            self.fanspeed = level
            print(f"{self.name} speed set to level {self.fanspeed}")
        else:
            print("Invalid fan speed! Use values between 1-5.")
    
    def get_status(self):
        return f"{self.name}: {'ON' if self.is_on else 'OFF'}, Speed: {self.fanspeed}"


class AC(Device):
    def __init__(self, name):
        super().__init__(name)
        self.temp = 24  # Default temperature
    
    def set_temperature(self):
        temp = int(input("Set AC TEMP (18°C - 26°C): "))
        if 18 <= temp <= 26:
            self.temp = temp
            print(f"{self.name} is set to {self.temp}°C")
        else:
            print("Invalid temperature! Use values between 18°C - 26°C.")
    
    def get_status(self):
        return f"{self.name}: {'ON' if self.is_on else 'OFF'}, Temperature: {self.temp}°C"


class Room:
    def __init__(self, name):
        self.name = name
        self.devices = []
    
    def add_device(self, device):
        self.devices.append(device)
        print(f"{device.name} has been added to {self.name}.")
    
    def control_all(self):
        control = input("Turn all devices (ON/OFF): ").strip().upper()
        if control not in ["ON", "OFF"]:
            print("Invalid input! Please enter ON or OFF.")
            return

        for device in self.devices:
            if control == "ON":
                device.turn_on()
            else:
                device.turn_off()
    
    def get_status(self):
        print(f"Status of {self.name}:")
        for device in self.devices:
            print(device.get_status())


class User:
    def __init__(self, name):
        self.name = name
    
    def control_device(self, device, action):
        if action == "ON":
            device.turn_on()
        elif action == "OFF":
            device.turn_off()
        else:
            print("Invalid action!")


# Menu for user interaction
def menu():
    print("\nSmart Home Automation System")
    room = Room(input("Enter Room Name: "))
    user = User(input("Enter User Name: "))
    
    while True:
        print("\nMenu:")
        print("1. Add Light")
        print("2. Add Fan")
        print("3. Add AC")
        print("4. Control All Devices")
        print("5. Check Room Status")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            device = Light(input("Enter Light Name: "))
            room.add_device(device)
        elif choice == "2":
            device = Fan(input("Enter Fan Name: "))
            room.add_device(device)
        elif choice == "3":
            device = AC(input("Enter AC Name: "))
            room.add_device(device)
        elif choice == "4":
            room.control_all()
        elif choice == "5":
            room.get_status()
        elif choice == "6":
            print("Exiting Smart Home System...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    menu()
