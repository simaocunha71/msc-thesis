def maximum(a, b):
    if(a > b):
        return a
    else:
        return b

# Unit tests
assert maximum(5,10) == 10
assert maximum(10,5) == 10
assert maximum(10,10) == 10

# Edge cases
assert maximum(10000000000, 20000000000) == 10000000000
assert maximum(0, 0) == 0
assert maximum(1000000000, -1000000000) == 1000000000

# Random cases
for i in range(1000):
    a = random.randint(0, 1000000000)
    b = random.randint(0, 1000000000)
    assert maximum(a, b) == max(a,b)

# Large cases
assert maximum(10**6, 2*10**6) == 2*10**6
assert maximum(10**7, 2*10**7) == 2*10**7
assert maximum(10**8, 2*10**8) == 2*10**8
assert maximum(10**9, 2*10**9) == 2*10**9

print("All test cases passed")





















































































































































