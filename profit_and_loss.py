import csv
from pathlib import Path

def compute_profit_difference(file_path):
    # Get the absolute path to the CSV file
    csv_path = Path("c:/Users/sohcj/OneDrive/Desktop/IGP 4 P4B Team A/P4B_ACC-1/csv_reports") / file_path

    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        previous_profit = 0
        profit_decrease_details = []
        highest_increase = 0
        highest_increase_day = None

        for row in reader:
            day, profit = int(row[0]), int(row[1])

            if profit < previous_profit:
                difference = previous_profit - profit
                profit_decrease_details.append((day, difference))
            else:
                increment = profit - previous_profit
                if increment > highest_increase:
                    highest_increase = increment
                    highest_increase_day = day

            previous_profit = profit

        return profit_decrease_details, highest_increase, highest_increase_day

# Create the relative file path to the CSV file
file_path = Path("profitsandloss.csv")

# Call the function and print the results
profit_decrease, highest_increase_value, highest_increase_day = compute_profit_difference(file_path)
