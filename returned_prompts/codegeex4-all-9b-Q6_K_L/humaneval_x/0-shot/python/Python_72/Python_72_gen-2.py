def will_it_fly(q,w):
    if sum(q) > w:
        return False
    else:
        return q == q[::-1]

print(will_it_fly([1, 2], 5))
print(will_it_fly([3, 2, 3], 1))
print(will_it_fly([3, 2, 3], 9))
print(will_it_fly([3], 5))