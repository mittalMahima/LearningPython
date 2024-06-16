def mergesort(arr, si, ei):
    if si >= ei:
        return
    mid = si + (ei - si) // 2
    mergesort(arr, si, mid)      # left
    mergesort(arr, mid + 1, ei)  # right
    merge(arr, si, mid, ei)

def merge(arr, si, mid, ei):
    temp = [0] * (ei - si + 1)
    i, j, k = si, mid + 1, 0

    while i <= mid and j <= ei:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= ei:
        temp[k] = arr[j]
        j += 1
        k += 1

    for k in range(len(temp)):
        arr[si + k] = temp[k]

def quicksort(arr, si, ei):
    if si >= ei:
        return
    pidx = partition(arr, si, ei)
    quicksort(arr, si, pidx - 1)  # left
    quicksort(arr, pidx + 1, ei)  # right

def partition(arr, si, ei):
    pivot = arr[ei]
    i = si - 1
    for j in range(si, ei):
        if arr[j] <= pivot:
            i += 1
            # swap
            arr[i], arr[j] = arr[j], arr[i]

    # swap pivot into correct place
    arr[i + 1], arr[ei] = arr[ei], arr[i + 1]
    return i + 1

if __name__ == "__main__":
    arr = [4, 2, 3, 6, 7, 8, 9, 0]
    # mergesort(arr, 0, len(arr) - 1)
    quicksort(arr, 0, len(arr) - 1)
    for elem in arr:
        print(elem, end=" ")
