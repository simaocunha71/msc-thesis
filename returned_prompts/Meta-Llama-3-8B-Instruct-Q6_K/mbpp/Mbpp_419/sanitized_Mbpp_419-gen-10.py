def round_and_sum(lst):
    total_sum = sum(round(num) for num in lst)
    print(total_sum * len(lst))
    return total_sum * len(lst)  # Return the total sum multiplied by the length of the list. This line is not necessary as per the problem statement. It was added for clarity.