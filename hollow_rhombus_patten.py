def hollow_rhombus(n):
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(" ", end="")
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()

if __name__ == "__main__":
    hollow_rhombus(5)
