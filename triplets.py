def print_triplets(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                print(f"Checking indices i={i}, j={j}, k={k}")  # Debug line
                if arr[i] != arr[j] and arr[j] != arr[k] and arr[i] != arr[k]:
                    if arr[i] + arr[j] + arr[k] == 0:
                        print(f"Triplet found: {arr[i]},{arr[j]},{arr[k]}")

if __name__ == "__main__":
    arr = [1, 2, -3, 1, 3, 0, 2, -2]
    print_triplets(arr)
