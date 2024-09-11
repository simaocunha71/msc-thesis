"""
def find_length(string):
    max_count = 0
    for i in range(len(string)):
        count = 0
        for j in range(i, len(string)):
            if string[j] == "1":
                count += 1
            else:
                count -= 1
            max_count = max(max_count, count)
    return max_count

# Test
print(find_length("11000010001"))  # 6
"""

def find_length(string):
    max_count = 0
    for i in range(len(string)):
        count = 0
        for j in range(i, len(string)):
            if string[j] == "1":
                count += 1
            else:
                count -= 1
            max_count = max(max_count, count)
    return max_count

# Test
print(find_length("11000010001"))  # 6


"""
def find_length(string):
    max_count = 0
    for i in range(len(string)):
        count = 0
        for j in range(i, len(string)):
            if string[j] == "1":
                count += 1
            else:
                count -= 1
            max_count = max(max_count, count)
    return max_count

# Test
print(find_length("11000010001"))  # 6


"""
def find_length(string):
    max_count = 0
    for i in range(len(string)):
        count = 0
        for j in range(i, len(string)):
            if string[j] == "1":
                count += 1
            else:
                count -= 1
            max_count = max(max_count, count)
    return max_count

# Test
print(find_length("11000010001"))  # 6


"""
def find_length(string):