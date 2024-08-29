
def check(n):
    return n == int(str(n)[::-1]) * 2 - 1

print(check(70))

# Output: False

