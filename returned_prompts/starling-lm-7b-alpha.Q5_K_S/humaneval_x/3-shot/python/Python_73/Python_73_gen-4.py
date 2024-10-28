    def count_odds(arr):
        return sum(1 for elem in arr if elem % 2 == 1)

    if len(arr) % 2 == 0:
        mid = len(arr) // 2 - 1
    else:
        mid = len(arr) // 2

    left_arr = arr[:mid]
    right_arr = arr[mid + 1:]
    left_odds = count_odds(left_arr)
    right_odds = count_odds(right_arr)
    return min(left_odds, right_odds)


