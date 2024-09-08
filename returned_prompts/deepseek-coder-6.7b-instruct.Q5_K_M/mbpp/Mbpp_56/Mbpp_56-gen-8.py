def check(num):
    reverse = int(str(num)[::-1])
    return num == 2 * reverse - 1

assert check(70) == False
assert check(131) == True
assert check(12321) == True
assert check(12421) == False
assert check(12521) == False
assert check(12621) == True

print("All test cases passed.")

