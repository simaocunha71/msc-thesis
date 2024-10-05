def will_it_fly(q, w):
    return q == q[::-1] and sum(q) <= w


q = [1, 2]
w = 5
print(will_it_fly(q, w))

q = [3, 2, 3]
w = 1
print(will_it_fly(q, w))

q = [3, 2, 3]
w = 9
print(will_it_fly(q, w))

q = [3]
w = 5
print(will_it_fly(q, w))