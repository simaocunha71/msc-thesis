def get_median(list1, list2, n):
    combined = sorted(list1 + list2)
    median_index = n // 2
    if n % 2 == 0:
        return (combined[median_index - 1] + combined[median_index]) / 2
    else:
        return combined[median_index]  # return the middle element if n is odd