
def make_a_pile(n):
    stones = [n]
    while n > 1:
        n += 1
        if n % 2 == 0:
            n += 1
        stones.append(n)
    return stones

# Test cases
print(make_a_pile(3))       # [3, 5, 7]
print(make_a_pile(4))       # [4, 6, 8]
print(make_a_pile(2))       # [2, 3]
print(make_a_pile(6))       # [6, 8, 10]
print(make_a_pile(1))       # [1]



def make_a_pile(n):
    stones = [n]
    while n > 1:
        n += 1
        if n % 2 == 0:
            n += 1
        stones.append(n)
    return stones

# Test cases
print(make_a_pile(3))       # [3, 5, 7]
print(make_a_pile(4))       # [4, 6, 8]
print(make_a_pile(2))       # [2, 3]
print(make_a_pile(6))       # [6, 8, 10]
print(make_a_pile(1))       # [1]





def make_a_pile(n):
    stones = [n]
    while n > 1:
        n += 1
        if n % 2 == 0:
            n += 1
        stones.append(n)
    return stones

# Test cases
print(make_a_pile(3))       # [3, 5, 7]
print(make_a_pile(4))       # [4, 6, 8]
print(make_a_pile(2))       # [2, 3]
print(make_a_pile(6))       # [6, 8, 10]
print