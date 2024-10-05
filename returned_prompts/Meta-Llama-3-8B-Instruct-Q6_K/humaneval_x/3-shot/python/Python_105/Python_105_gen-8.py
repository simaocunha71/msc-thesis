    def get_name(num):
        names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        return names[num]

    return [get_name(int(i)) for i in reversed(sorted([i for i in arr if 1 <= i <= 9]))] if arr else []
