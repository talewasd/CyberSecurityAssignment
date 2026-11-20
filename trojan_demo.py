
def calculate(num1, num2, activated):

    # Calculate the sum of the two numbers
    total = num1 + num2

    # If hidden behavior is already activated
    if activated:
        print("Hidden behavior already activated.")
        return 10, True

    # Activate hidden behavior when sum equals 10
    if total == 10:
        print("Hidden behavior activated!")
        activated = True
        return 10, activated

    # Return normal result
    return total, activated


def main():

    # Initially, hidden behavior is disabled
    activated = False

    # Keep running until the user exits
    while True:

        # Get two numbers from the user
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        # Calculate and update activation state
        result, activated = calculate(num1, num2, activated)

        # Display result
        print(f"The result is: {result}")

        # Ask whether to continue
        continue_choice = input("Do you want to continue? (y/n): ")

        if continue_choice.lower() == "n":
            break


if __name__ == "__main__":
    main()
