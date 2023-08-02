import csv

def compute_profit_difference(file_path):
    with open(file_path, 'r') as file:
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
compute_profit_difference("profitsandloss.csv")





<<<<<<< HEAD
=======
from pathlib import Path
import csv

def compute_profit_difference(file_path):
    with open(file_path, 'r') as file:
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






>>>>>>> 11ae9093d20058e6a429cb57aa6ba848ba0c6f88
