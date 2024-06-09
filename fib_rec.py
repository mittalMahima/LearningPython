def fibrecur(n):
    if n == 0 or n == 1:
        return n
    fib = fibrecur(n - 1) + fibrecur(n - 2)
    return fib

if __name__ == "__main__":
    n = int(input("Enter the term you want to calculate in fibonacci sequence: "))
    print(fibrecur(n))
