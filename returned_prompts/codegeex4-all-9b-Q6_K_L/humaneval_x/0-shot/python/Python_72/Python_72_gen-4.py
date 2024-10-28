def will_it_fly(q,w):
    if len(q) % 2 == 0:
        return sum(q) <= w
    else:
        return False

print(will_it_fly([1, 2], 5)) #➞ False 
print(will_it_fly([3, 2, 3], 1)) #➞ False
print(will_it_fly([3, 2, 3], 9)) #➞ True
print(will_it_fly([3], 5)) #➞ True