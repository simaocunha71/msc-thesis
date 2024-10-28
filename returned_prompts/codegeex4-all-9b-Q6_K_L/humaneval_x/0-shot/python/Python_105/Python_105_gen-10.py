def by_length(arr):
    digit_name = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return [digit_name[i] for i in sorted([i for i in arr if 1 <= i <= 9], reverse=True)]