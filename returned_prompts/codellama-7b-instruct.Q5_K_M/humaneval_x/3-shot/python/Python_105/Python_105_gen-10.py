    def is_int_between_1_and_9(x):
        return 1 <= x <= 9

    def digit_to_name(digit):
        if digit == 1:
            return "One"
        elif digit == 2:
            return "Two"
        elif digit == 3:
            return "Three"
        elif digit == 4:
            return "Four"
        elif digit == 5:
            return "Five"
        elif digit == 6:
            return "Six"
        elif digit == 7:
            return "Seven"
        elif digit == 8:
            return "Eight"
        elif digit == 9:
            return "Nine"

    sorted_arr = sorted(arr)
    reverse_sorted_arr = sorted_arr[::-1]

    result = []
    for i in reverse_sorted_arr:
        if is_int_between_1_and_9(i):
            result.append(digit_to_name(i))

    return result
