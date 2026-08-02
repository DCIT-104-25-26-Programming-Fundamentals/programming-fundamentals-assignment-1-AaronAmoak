# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#
# =============================================================================


def compute_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def compute_average(numbers):
    return compute_sum(numbers) / len(numbers)


def compute_max(numbers):
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val


def compute_min(numbers):
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val


def main():
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Error: The number of values must be positive.")
        return

    numbers = []
    for i in range(n):
        value = float(input(f"Enter number {i + 1}: "))
        numbers.append(value)

    print()
    print("Results:")
    print(f"Sum:     {compute_sum(numbers):g}")
    print(f"Average: {compute_average(numbers):g}")
    print(f"Maximum: {compute_max(numbers):g}")
    print(f"Minimum: {compute_min(numbers):g}")


if __name__ == "__main__":
    main()
