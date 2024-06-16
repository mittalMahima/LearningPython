def pairfriends(n):
    if n == 1 or n == 2:
        return n

    # single
    fnm1 = pairfriends(n - 1)
    # double
    fnm2 = pairfriends(n - 2)
    return fnm1 + (n - 1) * fnm2

if __name__ == "__main__":
    n=int(input("Enter the number of friends paired : "))
    print(pairfriends(n))
