import mean_calculator as mc


def display_menu():
    print("\nChoose which mean to calculate:")
    print("1. Arithmetic Mean")
    print("2. Geometric Mean")
    print("3. Harmonic Mean")
    print("4. Change Dataset")
    print("5. Exit")

def main():
    while True:
        print("\nPlease input a new dataset:")
        numbers = mc.get_numbers()

        if not numbers:
            print("No numbers entered. Exiting the program.")
            break

        while True:
            display_menu()
            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                result = mc.calculate_arithmetic_mean(numbers)
                print(f"Arithmetic Mean: {result}")
            elif choice == "2":
                result = mc.calculate_geometric_mean(numbers)
                print(f"Geometric Mean: {result}")
            elif choice == "3":
                result = mc.calculate_harmonic_mean(numbers)
                print(f"Harmonic Mean: {result}")
            elif choice == "4":
                break  # Break the inner loop to input a new dataset
            elif choice == "5":
                print("Exiting the program.")
                return  # Exit the program
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()