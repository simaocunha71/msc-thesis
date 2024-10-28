
def solution(lst):
    total = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and i % 2 != 0:
            total += lst[i]
    return total

# Alternative solution
def solution(lst):
    return sum(i for i in lst if i % 2 == 0 and i % 2 != 0)

# Alternative solution
def solution(lst):
    return sum([i for i in lst if i % 2 == 0 and i % 2 != 0])


# Alternative solution
def solution(lst):
    return sum(lst[i] for i in range(len(lst)) if lst[i] % 2 == 0 and i % 2 != 0)


# Alternative solution
def solution(lst):
    return sum([i for i in lst if i % 2 == 0][::2])

# Alternative solution
def solution(lst):
    return sum([i for i in lst if i % 2 == 0][::2])

# Alternative solution
def solution(lst):
    return sum(lst[i] for i in range(len(lst)) if lst[i] % 2 == 0)[::2]

# Alternative solution
def solution(lst):
    return sum(i for i in lst if i % 2 == 0)[::2]

# Alternative solution
def solution(lst):
    return sum([i for i in lst if i % 2 == 0][::2])

# Alternative solution
def solution(lst):
    return sum(lst[i] for i in range(len(lst)) if lst[i] % 2 == 0)[::2]

# Alternative solution
def solution(lst):
    return sum(i for i in lst if i % 2 == 0)[::2]

# Alternative solution
def solution(lst):
    return sum([i for i in lst if i % 2 == 0][::2])

# Alternative solution
def solution(lst):
    return sum(lst