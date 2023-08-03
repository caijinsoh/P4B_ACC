from pathlib import Path
import csv

def compute_cash_difference(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        cash_on_hand = []

        for row in reader:
            cash_on_hand.append([int(row[0]), int(row[1])])

    deficit_cash = []
    highest_surplus = 0
    highest_surplus_day = None

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
print("hello")
print("bye")
print("dog")
print("hi")