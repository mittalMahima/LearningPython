def floyd_tri(n):
    counter = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(counter, end=" ")
            counter += 1
        print()

if __name__ == "__main__":
    floyd_tri(10)
