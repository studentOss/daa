# Practical 3: Fractional Knapsack using Greedy Method

def fractional_knapsack(weights, values, capacity):

    items = []

    # Calculate value/weight ratio
    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i], i + 1))

    # Sort items according to ratio in descending order
    items.sort(reverse=True)

    total_value = 0

    print("\nSelected Items:")

    for ratio, weight, value, item_no in items:

        if capacity == 0:
            break

        # Complete item can be selected
        if weight <= capacity:

            capacity -= weight
            total_value += value

            print("Item", item_no,
                  "-> Full item",
                  "| Weight =", weight,
                  "| Value =", value,
                  "| Ratio =", round(ratio, 2))

        # Only fraction of item can be selected
        else:

            fraction = capacity / weight
            selected_value = value * fraction

            total_value += selected_value

            print("Item", item_no,
                  "-> Fraction =", round(fraction, 2),
                  "| Weight =", capacity,
                  "| Value =", round(selected_value, 2),
                  "| Ratio =", round(ratio, 2))

            capacity = 0

    print("\nMaximum Value:", round(total_value, 2))


# Main program

n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):

    weight = float(input(f"Enter weight of item {i + 1}: "))
    value = float(input(f"Enter value of item {i + 1}: "))

    weights.append(weight)
    values.append(value)

capacity = float(input("Enter knapsack capacity: "))

fractional_knapsack(weights, values, capacity)