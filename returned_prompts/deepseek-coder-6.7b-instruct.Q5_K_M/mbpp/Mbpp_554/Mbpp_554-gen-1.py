
def Split(lst):
    return [i for i in lst if i % 2 != 0]

print(Split([1,2,3,4,5,6]))
assert Split([1,2,3,4,5,6]) == [1,3,5]

# 2.
