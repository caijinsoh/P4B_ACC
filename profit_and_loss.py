import csv
from pathlib import Path

def compute_profit_difference(file_path):
<<<<<<< HEAD
    # Get the absolute path to the CSV file
    csv_path = Path("c:/Users/sohcj/OneDrive/Desktop/IGP 4 P4B Team A/P4B_ACC-1/csv_reports") / file_path

    with open(csv_path, 'r') as file:
=======
    # Opens the CSV file containing profit data and initialize variables for calculations.
    with open(file_path, 'r') as file:
>>>>>>> 01a94e30135ee8229e884772e3b5216c052718eb
        reader = csv.reader(file)
        next(reader)  # Skip header

        previous_profit = 0
        profit_decrease_details = []  # List to store days and corresponding profit decreases.
        highest_increase = 0  # Variable to keep track of the highest profit increase.
        highest_increase_day = None  # Variable to store the day with the highest profit increase.

        # Loop through each row in the CSV file to compute profit differences.
        for row in reader:
            day, profit = int(row[0]), int(row[1])

            if profit < previous_profit:
                # Calculates the profit decrease and store the day and difference in profit_decrease_details.
                difference = previous_profit - profit
                profit_decrease_details.append((day, difference))
            else:
                # Calculates the profit increase and update the highest_increase and highest_increase_day if applicable.
                increment = profit - previous_profit
                if increment > highest_increase:
                    highest_increase = increment
                    highest_increase_day = day

            previous_profit = profit  # Updates the previous_profit for the next iteration.

        return profit_decrease_details, highest_increase, highest_increase_day

<<<<<<< HEAD
# Create the relative file path to the CSV file
file_path = Path("profitsandloss.csv")

# Call the function and print the results
profit_decrease, highest_increase_value, highest_increase_day = compute_profit_difference(file_path)
=======
# Calls the function with the file name "profitsandloss.csv" to compute profit differences.
compute_profit_difference("profitsandloss.csv")
>>>>>>> 01a94e30135ee8229e884772e3b5216c052718eb
