def will_it_fly(q,w):
    if sum(q) > w:
        return False
    if q == q[::-1]:
        return True
    return False

print(will_it_fly([1, 2], 5)) # ➞ False 
print(will_it_fly([3, 2, 3], 1)) # ➞ False
print(will_it_fly([3, 2, 3], 9)) # ➞ True
print(will_it_fly([3], 5)) # ➞ True

#Explanation:
#- First, we check if the sum of the elements in the list `q` is greater than the maximum possible weight `w`. If it is, we return False because the object `q` will not fly.
#- Next, we check if the list `q` is a palindrome, meaning it reads the same forwards and backwards. If it is, we return True because the object `q` will fly.
#- If neither of the above conditions are met, we return False because the object `q` will not fly.