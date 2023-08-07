from pathlib import Path 
import csv

def compute_cash_differnce(file_path):
    # Read data from the CSV file and store it in an empty list-cash_on_hand.
    with open (file_path,"r") as file:
        reader = csv.reader(file)
        next(reader) # Skip reader

        cash_on_hand = []
        
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
        