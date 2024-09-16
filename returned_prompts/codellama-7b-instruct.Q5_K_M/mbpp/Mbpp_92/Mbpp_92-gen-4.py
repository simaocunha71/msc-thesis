def is_undulating(num):
    return "1" * len(str(num)) == str(num)

# OR

def is_undulating(num):
    return str(num) == "1" * len(str(num))

# OR

def is_undulating(num):
    return num == int("1" * len(str(num)))


