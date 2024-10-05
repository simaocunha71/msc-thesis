    def num_to_name(num):
        names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        return names[num]

    arr = [num_to_name(num) if 1 <= num <= 9 else "" for num in arr]
    arr.sort()
    arr = arr[::-1]
    return [name for name in arr if name]  # remove empty strings


