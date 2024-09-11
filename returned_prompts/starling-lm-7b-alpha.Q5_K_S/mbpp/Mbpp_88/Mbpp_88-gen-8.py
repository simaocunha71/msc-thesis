def freq_count(arr):
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


# Testing
print(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]))
print(freq_count([1,1,2,2,3,3,4,4]))
print(freq_count([5,6,7,6,7,5,6,7]))
print(freq_count([1,2,3,4,5]))
print(freq_count([]))
print(freq_count([1]))

# Assertion Testing
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
assert freq_count([1,1,2,2,3,3,4,4])==({1: 2, 2: 2, 3: 2, 4: 2})
assert freq_count([5,6,7,6,7,5,6,7])==({5: 2, 6: 3, 7: 3})
assert freq_count([1,2,3,4,5])==({1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
assert freq_count([])==({})
assert freq_count([1])==({1: 1})



# Time Complexity: O(n)
# Space Complexity: O(n)





























"""
def freq_count(arr):
    d = {}
    for i in