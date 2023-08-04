import overheads
import cash_on_hand
import profit_and_loss

def main():
    highest_category, highest_overhead_percentage = overheads.find_highest_overhead_category("Overhead.csv")
    deficit_cash, highest_surplus, highest_surplus_day = cash_on_hand.compute_cash_difference("cashonhand.csv")
    profit_decrease_details, highest_increase, highest_increase_day = profit_and_loss.compute_profit_difference('profitsandloss.csv')

    with open("summary_report.txt", "w") as file:
        file.write(f"[HIGHEST OVERHEAD] {highest_category.split(',')[0]}: {round(highest_overhead_percentage, 2)}%\n")

        if deficit_cash:
            for day, amount in deficit_cash:
                file.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD {amount} \n")  # Format changed here
        else:
            file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            file.write(f"[HIGHEST CASH SURPLUS] DAY: {highest_surplus_day}, AMOUNT: USD {highest_surplus}")

        if profit_decrease_details:
            for day, amount in profit_decrease_details:
                file.write(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD {amount}\n")
        else:
            file.write(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY.\n")
            file.write(f"[HIGHEST NET PROFIT SURPLUS] DAY: {highest_increase_day}, AMOUNT: USD {highest_increase}")

if __name__ == "__main__":
    main()








