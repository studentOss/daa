# Practical 4: 0/1 Knapsack using Dynamic Programming

def knapsack(weights, values, capacity):

    n = len(weights)

    # Create DP table
    # Rows = n + 1
    # Columns = capacity + 1
    T = [[0 for _ in range(capacity + 1)]
         for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):

        for j in range(1, capacity + 1):

            if weights[i - 1] <= j:

                T[i][j] = max(
                    T[i - 1][j],
                    values[i - 1] + T[i - 1][j - weights[i - 1]]
                )

            else:

                T[i][j] = T[i - 1][j]

    # Display DP table
    print("\nDP Table:")

    for row in T:
        print(row)

    # Maximum value
    maximum_value = T[n][capacity]

    print("\nMaximum Value:", maximum_value)

    # Find selected items
    selected_items = []

    j = capacity

    for i in range(n, 0, -1):

        if T[i][j] != T[i - 1][j]:

            selected_items.append(i)
            j = j - weights[i - 1]

    selected_items.reverse()

    print("Selected Items:", selected_items)


# Main program

n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):

    weight = int(input(f"Enter weight of item {i + 1}: "))
    value = int(input(f"Enter value of item {i + 1}: "))

    weights.append(weight)
    values.append(value)

capacity = int(input("Enter knapsack capacity: "))

knapsack(weights, values, capacity)