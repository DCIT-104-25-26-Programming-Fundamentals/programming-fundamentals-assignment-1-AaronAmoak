# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
#
# REQUIREMENTS
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
#
# =============================================================================


def print_table(num):
    print(f"Multiplication Table for {num}:")
    for i in range(1, 13):
        print(f"{num}  x  {i:2}  =  {num * i}")


def print_tables_up_to(n):
    for num in range(1, n + 1):
        print_table(num)
        if num != n:
            print("---------------------------")


def main():
    # ---------------- PART A ----------------
    number = int(input("Enter a number: "))
    print()
    print_table(number)

    # ---------------- PART B ----------------
    n = int(input("\nEnter N (for tables 1 to N): "))

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    print()
    print_tables_up_to(n)


if __name__ == "__main__":
    main()
