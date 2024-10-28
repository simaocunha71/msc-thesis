def round_and_sum(lst):
    total_sum = sum(round(num) for num in lst)
    return total_sum * len(lst)  # This will return the total sum multiplied by the length of the list