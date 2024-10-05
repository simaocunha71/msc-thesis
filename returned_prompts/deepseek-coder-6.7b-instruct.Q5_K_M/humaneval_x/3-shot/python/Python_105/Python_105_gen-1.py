    words = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return [words[i-1] for i in sorted(arr)[::-1] if 1 <= i <= 9]


