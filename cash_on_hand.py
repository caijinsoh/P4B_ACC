from pathlib import Path 
import csv

def compute_cash_difference(file_path):
    # Get the absolute path to the CSV file
    csv_path = Path("csv_reports") / file_path

    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        next(reader) # Skip reader

        cash_on_hand = []  # Create empty list to store values
        
        for row in reader:
            cash_on_hand.append([int(row[0]), int(row[1])])

    # Initialize empty lists and variables to store deficit cash and highest surplus.
    deficit_cash = []
    deficit_cash = []
    highest_surplus = 0
    highest_surplus_day = None

    # Loop through the cash_on_hand list to calculate the dificit cash and find the highest surplus.
    for i in range(1, len(cash_on_hand)):
        day, cash = cash_on_hand[i]
        prev_day, prev_cash = cash_on_hand[i - 1]
        difference = cash - prev_cash

        if difference < 0:
            deficit_cash.append((day, abs(difference)))  # Use abs() to make it positive
        else:
            if difference > highest_surplus:
                highest_surplus = difference
                highest_surplus_day = day

    return deficit_cash, highest_surplus, highest_surplus_day

deficit_cash, highest_surplus_value, highest_surplus_day = compute_cash_difference("cashonhand.csv")
