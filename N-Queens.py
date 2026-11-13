# Practical 5: N-Queens Problem using Backtracking

def is_safe(board, row, col, n):

    # Check the same row
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i = row + 1
    j = col - 1

    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve(board, col, n):

    # All queens are placed
    if col == n:
        return True

    # Try every row in the current column
    for row in range(n):

        if is_safe(board, row, col, n):

            # Place queen
            board[row][col] = 1

            # Recursively place queen in next column
            if solve(board, col + 1, n):
                return True

            # Backtrack: remove queen
            board[row][col] = 0

    return False


# Main program

n = int(input("Enter the value of N: "))

# Create N x N matrix filled with 0
board = [[0 for _ in range(n)] for _ in range(n)]

if solve(board, 0, n):

    print("\nN-Queens Solution:")

    for row in board:
        print(*row)

else:
    print("\nNo solution exists.")