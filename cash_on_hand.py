
        
        # If the difference is negative, it means there is a deficit cash on that day.
        # Append the day and the absolute value of the difference to the deficit_cash list.
        if difference < 0:
            deficit_cash.append((day, abs(difference)))  # Use abs() to make it positive
        else:
            # If the difference is positive, update the highest_surplus and highest_surplus_day
            # if the current difference is greater than the previous highest_surplus.
            if difference > highest_surplus:
                highest_surplus = difference
                highest_surplus_day = day

    # Return the deficit_cash list, highest_surplus amount, and the day with the highest surplus.
    return deficit_cash, highest_surplus, highest_surplus_day