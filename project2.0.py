def pattern_generator():
    print("\n" + "=" * 50)
    print("           MODULE 1: PATTERN GENERATOR            ")
    print("=" * 50)

    try:
        rows = int(input("Enter the number of rows for the patterns: "))
        if rows <= 0:
            print("Please enter a positive integer greater than zero.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return

    # Pattern 1: Right-Angled Triangle using nested FOR loops
    print(f"\n1. Right-Angled Triangle (Generated using FOR loops):")
    print("-" * 50)
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

    # Pattern 2: Right-Angled Triangle using nested WHILE loops
    print(f"\n2. Right-Angled Triangle (Generated using WHILE loops):")
    print("-" * 50)
    row_idx = 1
    while row_idx <= rows:
        col_idx = 1
        while col_idx <= row_idx:
            print("*", end=" ")
            col_idx += 1
        print()
        row_idx += 1


def number_analyzer():
    print("\n" + "=" * 50)
    print("            MODULE 2: NUMBER ANALYZER             ")
    print("=" * 50)

    try:
        start_num = int(input("Enter the starting number: "))
        end_num = int(input("Enter the ending number: "))
    except ValueError:
        print("Invalid input! Please enter valid integers.")
        return

    if start_num > end_num:
        print(
            "Starting number should be less than or equal to the ending number."
        )
        return

    print("\n--- Number Breakdown (Odd / Even Check) ---")
    total_sum = 0

    # Iterating using for loop with range()
    for num in range(start_num, end_num + 1):
        if num % 2 == 0:
            status = "Even"
        else:
            status = "Odd"

        print(f"Number: {num:4d} | Status: {status}")
        total_sum += num

    print("-" * 50)
    print(f"Sum of all numbers from {start_num} to {end_num}: {total_sum}")


def main():
    # ----------------------------------------------------
    # WELCOME MESSAGE
    # ----------------------------------------------------
    print("=" * 60)
    print("     WELCOME TO THE PATTERN & NUMBER ANALYZER APP      ")
    print("=" * 60)
    print("This program allows you to:")
    print("  1. Generate right-angled triangle patterns using nested")
    print("     'for' and 'while' loops.")
    print("  2. Analyze a user-defined range of numbers to check for")
    print("     Odd/Even status and compute the total sum.")
    print("=" * 60)

    # Execute Module 1: Pattern Generation
    pattern_generator()

    # Execute Module 2: Number Analysis
    number_analyzer()

    # ----------------------------------------------------
    # THANK YOU MESSAGE
    # ----------------------------------------------------
    print("\n" + "=" * 60)
    print("    Thank you for using the Pattern & Number Analyzer!   ")
    print("             Have a great day ahead!                    ")
    print("=" * 60)


if __name__ == "__main__":
    main()
