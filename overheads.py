from pathlib import Path
import csv

def find_highest_overhead_category(filename):
    highest_category = None
    highest_overhead = 0
    total_expense = 0
    highest_overhead_percentage = 0

    # Get the absolute path to the CSV file
    csv_path = Path("csv_reports") / filename

    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            category = row[0]
            expense = int(row[1])

            total_expense += expense

            if expense > highest_overhead:
                highest_overhead = expense
                highest_category = category

            highest_overhead_percentage = (highest_overhead / total_expense) * 100

    return highest_category, highest_overhead_percentage

# Call the function
result_category, result_percentage = find_highest_overhead_category("Overhead.csv")

