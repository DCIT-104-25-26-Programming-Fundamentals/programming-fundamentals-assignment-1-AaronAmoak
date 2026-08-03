# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
#
# REQUIREMENTS
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#
# =============================================================================


def print_fibonacci(n):
    a, b = 0, 1
    terms = []
    for _ in range(n):
        terms.append(str(a))
        a, b = b, a + b
    print("Fibonacci sequence: " + " ".join(terms))


def is_fibonacci(num):
    if num < 0:
        return False

    a, b = 0, 1
    if num == a:
        return True

    while a <= num:
        if a == num:
            return True
        a, b = b, a + b

    return False


def main():
    # ---------------- PART A ----------------
    n = int(input("How many terms? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        print_fibonacci(n)

    # ---------------- PART B ----------------
    num = int(input("Enter a number to check: "))

    if is_fibonacci(num):
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()
