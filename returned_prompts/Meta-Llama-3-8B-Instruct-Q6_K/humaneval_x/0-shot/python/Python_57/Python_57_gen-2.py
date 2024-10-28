def monotonic(l: list):
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))
# or
def monotonic(l: list):
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1)) and l[0] <= l[-1] or l[0] >= l[-1]
# or
def monotonic(l: list):
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    return increasing or decreasing
# or
def monotonic(l: list):
    return (all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))) and (l[0] <= l[-1] or l[0] >= l[-1])
# or
def monotonic(l: list):
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1)) and l[0] <= l[-1]
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1)) and l[0] >= l[-1]
    return increasing or decreasing
# or
def monotonic(l: list):
    if all(l[i] <= l[i+1] for i in range(len(l)-1)):
        return l[0] <= l[-1]
    elif all(l[i] >= l[i+1] for i in range(len(l)-1)):
        return l[0] >= l[-1]
    else:
        return False
# or
def monotonic(l: list):
    if all(l[i] <= l[i+1] for i in range(len(l)-1)):
        return l[0] <= l[-1]
    elif all(l[i] >= l[i+1] for i in range(len(l)-1)):
        return l[0] >= l[-1]
    else:
        return False
# or
def monotonic(l: list):
    if all(l[i] <= l