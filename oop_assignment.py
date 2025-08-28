# -----------------------------
# Assignment 1: Design Your Own Class
# -----------------------------

# Base Class
class Smartphone:
    def __init__(self, brand, model, price):
        self.__brand = brand      # private attribute (encapsulation)
        self.__model = model
        self.price = price

    # Getter for brand
    def get_brand(self):
        return self.__brand

    # Getter for model
    def get_model(self):
        return self.__model

    # Method to display info
    def display_info(self):
        print(f"Smartphone: {self.__brand} {self.__model}, Price: ${self.price}")

    def make_call(self, number):
        print(f"Calling {number} from {self.__brand} {self.__model}...")


# Derived Class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        # Call parent constructor
        super().__init__(brand, model, price)
        self.gpu = gpu

    # Method overriding (polymorphism)
    def display_info(self):
        print(f"Gaming Smartphone: {self.get_brand()} {self.get_model()}, GPU: {self.gpu}, Price: ${self.price}")

    def play_game(self, game_name):
        print(f"Playing {game_name} smoothly with {self.gpu} GPU!")


# -----------------------------
# Activity 2: Polymorphism Challenge
# -----------------------------

class Animal:
    def move(self):
        pass  # abstract-like method (to be overridden)


class Dog(Animal):
    def move(self):
        print("Dog is running!")


class Fish(Animal):
    def move(self):
        print("Fish is swimming!")


class Bird(Animal):
    def move(self):
        print("Bird is flying!")


# -----------------------------
# Main Program (Testing)
# -----------------------------
if __name__ == "__main__":
    # Assignment 1
    phone1 = Smartphone("Samsung", "S24 Ultra", 1200)
    phone1.display_info()
    phone1.make_call("08012345678")

    print()

    gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 1500, "Adreno 730")
    gaming_phone.display_info()
    gaming_phone.play_game("PUBG Mobile")

    print("\n--- Polymorphism Challenge ---")
    animals = [Dog(), Fish(), Bird()]
    for animal in animals:
        animal.move()
