    def get_name(num):
        return ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][num]

    return [get_name(num) for num in sorted([num for num in arr if 1 <= num <= 9])][::-1]