from pathlib import Path
import csv
 # Read data from the CSV file and store it in a list called cash_on_hand.
def compute_cash_difference(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        cash_on_hand = []

        for row in reader:
            cash_on_hand.append([int(row[0]), int(row[1])])

    # Initialize empty lists and variables to store deficit cash and highest surplus.
    deficit_cash = []
    highest_surplus = 0
    highest_surplus_day = None

    # Loop through the cash_on_hand list to calculate the deficit cash and find the highest surplus.
    for i in range(1, len(cash_on_hand)):
        day, cash = cash_on_hand[i]
        prev_day, prev_cash = cash_on_hand[i - 1]
        difference = cash - prev_cash

        # If the difference is negative, it means there is a deficit cash on that day.
        # Append the day and the absolute value of the difference to the deficit_cash list.
        if difference < 0:
            deficit_cash.append((day, abs(difference)))  # Use abs() to make it positive
        else:
            # If the difference is positive, update the highest_surplus and highest_surplus_day
            # if the current difference is greater than the previous highest_surplus.
            if difference > highest_surplus:
                highest_surplus = difference
                highest_surplus_day = day

    return deficit_cash, highest_surplus, highest_surplus_day
