def will_it_fly(q,w):
    return q==q[::-1] and sum(q)<=w

print(will_it_fly([1, 2], 5)) # False 
print(will_it_fly([3, 2, 3], 1)) # False
print(will_it_fly([3, 2, 3], 9)) # True
print(will_it_fly([3], 5)) # True

B:
def will_it_fly(q,w):
    return q==q[::-1] and sum(q)<=w

print(will_it_fly([1, 2], 5)) # False 
print(will_it_fly([3, 2, 3], 1)) # False
print(will_it_fly([3, 2, 3], 9)) # True
print(will_it_fly([3], 5)) # True

C:
def will_it_fly(q,w):
    return q==q[::-1] and sum(q)<=w

print(will_it_fly([1, 2], 5)) # False 
print(will_it_fly([3, 2, 3], 1)) # False
print(will_it_fly([3, 2, 3], 9)) # True
print(will_it_fly([3], 5)) # True

D:
def will_it_fly(q,w):
    return q==q[::-1] and sum(q)<=w

print(will_it_fly([1, 2], 5)) # False 
print(will_it_fly([3, 2, 3], 1)) # False
print(will_it_fly([3, 2, 3], 9)) # True
print(will_it_fly([3], 5)) # True