from pathlib import Path
import csv

def find_highest_overhead_category(filename):
    # Initializes variables to store the highest overhead category and related data.
    highest_category = None
    highest_overhead = 0
    total_expense = 0
    highest_overhead_percentage = 0

<<<<<<< HEAD
    # Get the absolute path to the CSV file
    csv_path = Path("csv_reports") / filename

    with open(csv_path, 'r') as file:
=======
    # Opens the CSV file and read its contents.
    with open(filename, 'r') as file:
>>>>>>> 01a94e30135ee8229e884772e3b5216c052718eb
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        # Loops through each row in the CSV file.
        for row in reader:
            category = row[0]  # Extracts the category from the first column.
            expense = int(row[1])  # Converts the expense from the second column to an integer.

            total_expense += expense  # Accumulates the total expenses.

            # Checks if the current expense is higher than the highest overhead found so far.
            # If it is, it updates the highest overhead and the corresponding category.
            if expense > highest_overhead:
                highest_overhead = expense
                highest_category = category

            # Calculates the highest overhead percentage based on the current highest overhead and total expenses.
            highest_overhead_percentage = (highest_overhead / total_expense) * 100

    # Returns the highest overhead category and its percentage.
    return highest_category, highest_overhead_percentage

<<<<<<< HEAD
# Call the function
result_category, result_percentage = find_highest_overhead_category("Overhead.csv")

=======
# Calls the function with the file name "Overhead.csv" to find the highest overhead category and percentage.
find_highest_overhead_category("Overhead.csv")

print("bye")
>>>>>>> 01a94e30135ee8229e884772e3b5216c052718eb
