def diamond_pattern(n):
    # First half of the diamond
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(1, n - i + 1):
            print(" ", end="")
        # Print stars
        for j in range(1, 2 * i):
            print("*", end="")
        print()
    
    # Second half of the diamond
    for i in range(n, 0, -1):
        # Print leading spaces
        for j in range(1, n - i + 1):
            print(" ", end="")
        # Print stars
        for j in range(1, 2 * i):
            print("*", end="")
        print()

if __name__ == "__main__":
    a=int(input("Enter size for pattern: "))
    diamond_pattern(a)
