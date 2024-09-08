
def pos_count(lst):
    return sum(1 for i in lst if i > 0)

print(pos_count([1,-2,3,-4])) # 2

# Alternative Solution
def pos_count(lst):
    count = 0
    for i in lst:
        if i > 0:
            count += 1
    return count

print(pos_count([1,-2,3,-4])) # 2

# Alternative Solution
def pos_count(lst):
    return len([i for i in lst if i > 0])

print(pos_count([1,-2,3,-4])) # 2

