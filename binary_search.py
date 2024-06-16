def binary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == key:
            return mid

        elif arr[mid] < key:
            left = mid + 1

        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    print("Enter the elements of array in increasing order or decreasing order:")
    input_str = input()
    arr = list(map(int, input_str.split()))  # Split input by spaces and convert to int list

    print("Enter the key to search:")
    key = int(input())

    index = binary_search(arr, key)
    if index == -1:
        print("Key not found")
    else:
        print(f"Key is found at index {index}")
