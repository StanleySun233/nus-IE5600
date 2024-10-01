def get_number():
    """Prompts user to input a valid number and returns it as int or float, or None if input is empty."""
    while True:
        user_input = input("Enter a number (or press Enter to finish): ").strip()

        if user_input == "":
            return None

        try:
            if "." in user_input:
                return float(user_input)
            else:
                return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_numbers():
    """Uses get_number() to collect a list of numbers from the user."""
    numbers = []

    while True:
        num = get_number()
        if num is None:
            break
        numbers.append(num)

    return numbers


def calculate_arithmetic_mean(nums):
    """Calculates the arithmetic mean of a list of numbers."""
    if not nums:
        return None
    return sum(nums) / len(nums)


def calculate_geometric_mean(nums):
    """Calculates the geometric mean of a list of numbers."""
    if not nums:
        return None

    product = 1
    for num in nums:
        product *= num

    return product ** (1 / len(nums))


def calculate_harmonic_mean(nums):
    """Calculates the harmonic mean of a list of numbers."""
    if not nums:
        return None

    reciprocal_sum = sum(1 / num for num in nums)

    return len(nums) / reciprocal_sum
