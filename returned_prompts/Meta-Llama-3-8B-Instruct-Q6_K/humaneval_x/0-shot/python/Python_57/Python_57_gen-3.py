def monotonic(l: list):
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))
#or
def monotonic(l: list):
    return (all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1)))
#or
def monotonic(l: list):
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1)) and l[0] >= l[-1] or l[0] <= l[-1]
#or
def monotonic(l: list):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True
#or
def monotonic(l: list):
    if len(l) < 2:
        return True
    if l[0] > l[1]:
        for i in range(2, len(l)):
            if l[i-1] > l[i]:
                return False
    else:
        for i in range(2, len(l)):
            if l[i-1] < l[i]:
                return False
    return True
#or
def monotonic(l: list):
    return all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))
#or
def monotonic(l: list):
    return (all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))) and (l[0] >= l[-1] or l[0] <= l[-1])
#or
def monotonic(l: list):
    if len(l) < 2:
        return True
    if l[0] > l[1]:
        return all(x <= y for x, y in zip(l[1:], l[2:]))
    else:
        return all(x >= y for x, y in zip(l[1:], l[2:]))
#or
def monotonic(l: list):
    return (all