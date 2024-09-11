def count_reverse_pairs(strings):
    # Your code here
    count = 0
    for s in strings:
        reverse = s[::-1]
        if reverse in strings:
            count += 1
    return count

# assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2

def count_reverse_pairs(strings):
    # Your code here
    count = 0
    for i in range(len(strings)):
        if strings[i][::-1] in strings:
            count += 1
    return count

# assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2

def count_reverse_pairs(strings):
    # Your code here
    count = 0
    for s in strings:
        if s[::-1] in strings:
            count += 1
    return count

# assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2

def count_reverse_pairs(strings):
    # Your code here
    count = 0
    for i in range(len(strings)):
        s = strings[i]
        if s[::-1] in strings:
            count += 1
    return count

# assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2

def count_reverse_pairs(strings):
    # Your code here
    count = 0
    for i in range(len(strings)):
        s = strings[i]
        if s[::-1] in strings:
            count += 1
    return count

# assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2

def count_reverse_pairs(strings):
    # Your code here
    count = 0
    for s in strings:
        if s[::-1] in strings:
