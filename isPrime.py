def is_prime(n):
    is_prime = True
    if n == 2:
        print("number is prime")
        return is_prime

    for i in range(2, n - 1):
        if n % i == 0:
            is_prime = False
            break  # Early exit if a divisor is found

    return is_prime

if __name__ == "__main__":
    a = int(input("Enter a number: "))
    print(is_prime(a))
