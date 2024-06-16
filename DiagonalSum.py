def diagonal_sum(matrix):
    sum = 0
    n = len(matrix)
    for i in range(n):
        sum += matrix[i][i]
        if i != n - 1 - i:  # To avoid overlapping condition
            sum += matrix[i][n - 1 - i]
    return sum

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Diagonal sum is ")
    print(diagonal_sum(matrix))
