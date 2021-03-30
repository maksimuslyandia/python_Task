import os
from lib.client import Client


OPERATING_SYSTEM = os.name

# If we are on windows
if OPERATING_SYSTEM == "nt":
    clear = lambda: os.system("cls")

else:
    clear = lambda: os.system("clear")

MAIN_MENU_OPTIONS = ["1", "2", "3"]


def display_main_menu():
    print("\n1 - List available cars for rent.")
    print("2 - Rent car/s.")
    print("3 - Exit.")


def main_loop():
    client = Client()

    # Clearing out the previous command line outputs
    clear()
    print("\nWelcome! These are your options at our place:")
    while True:
        display_main_menu()
        main_menu_choice = input("Enter your choice:")
        
        if main_menu_choice in MAIN_MENU_OPTIONS:

            if main_menu_choice == "1":
                client.list_cars()

            elif main_menu_choice == "2":
                total_price = client.choose()
                print(f"Total price: ${total_price}")

            elif main_menu_choice == "3":
                print("Exiting...")
                exit()

        else:
            print("Invalid choice, try again!")


if __name__ == "__main__":
    main_loop()