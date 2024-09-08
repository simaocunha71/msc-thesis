def minimum(x, y):
    if x > y:
        return y
    else:
        return x

print(minimum(1,2))

# Alternatively, you can use the built-tin min function
def minimum_v2(x, y):
    return min(x, y)

print(minimum_v2(1,2))

# Another alternative is to use a ternary expression
def minimum_v3(x, y):
    return x if x > y else y

print(minimum_v3(1,2))

# 