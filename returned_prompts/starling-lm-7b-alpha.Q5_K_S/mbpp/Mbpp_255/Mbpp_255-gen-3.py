def combinations_colors(colors,n):
    result = []
    for i in range(len(colors)):
        result.append(tuple(colors[i] for _ in range(n)))
    return result

# assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
# print(combinations_colors(["Red","Green","Blue"],1))

def combinations_colors(colors,n):
    result = []
    if n==0:
        result.append(tuple())
    else:
        for i in range(len(colors)):
            for combination in combinations_colors(colors[:i]+colors[i+1:],n-1):
                result.append((colors[i],) + combination)
    return result

# assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
# print(combinations_colors(["Red","Green","Blue"],1))

def combinations_colors(colors,n):
    result = []
    for i in range(len(colors)):
        for c in combinations_colors(colors[:i]+colors[i+1:],n-1):
            result.append((colors[i],) + c)
    return result

# assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
# print(combinations_colors(["Red","Green","Blue"],1))

def combinations_colors(colors,n):
    result = []
    if n==0:
        result.append(tuple())
    else:
        for c in colors:
            for combination in combinations_colors(colors,n-1):
                result.append((c,) + combination)
    return result

# assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
# print(combinations_colors(["Red","Green","Blue"],1))

def combinations_colors(colors,n):
    result = []
    if n==0:
        result.append(tuple())
