import overheads
import cash_on_hand
import profit_and_loss


def main():
    # Calculates the highest overhead category and its percentage from "Overhead.csv" using the overheads module.
    highest_category, highest_overhead_percentage = overheads.find_highest_overhead_category("Overhead.csv")

    # Calculates deficit cash and the highest surplus from "cashonhand.csv" using the cash_on_hand module.
    deficit_cash, highest_surplus, highest_surplus_day = cash_on_hand.compute_cash_difference("cashonhand.csv")

    # Calculates profit decrease details and the highest increase from "profitsandloss.csv" using the profit_and_loss module.
    profit_decrease_details, highest_increase, highest_increase_day = profit_and_loss.compute_profit_difference('profitsandloss.csv')

    # Writes the results to the "summary_report.txt" file.
    with open("summary_report.txt", "w") as file:
        file.write(f"[HIGHEST OVERHEAD] {highest_category.split(',')[0].upper()}: {round(highest_overhead_percentage, 2)}%\n")

        # Checks if there is any deficit cash. If so, write each deficit to the file.
        if len(deficit_cash) != 0:
            for day, amount in deficit_cash:
                file.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD {amount} \n")
        else:
            # If there is no deficit cash, this indicates there is a surplus and write the highest surplus to the file.
            file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            file.write(f"[HIGHEST CASH SURPLUS] DAY: {highest_surplus_day}, AMOUNT: USD {highest_surplus}\n")

        # Checks if there are any profit decrease details. If so, write each detail to the file.
        if len(profit_decrease_details) != 0:
            for day, amount in profit_decrease_details:
                file.write(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD {amount}\n")
        else:
            # If there are no profit decreases, this indicates there is a surplus and write the highest increase to the file.
            file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY.\n")
            file.write(f"[HIGHEST NET PROFIT SURPLUS] DAY: {highest_increase_day}, AMOUNT: USD {highest_increase}\n")

if __name__ == "__main__":
    main()








