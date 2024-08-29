def unique_digits(x):
    return sorted([i for i in x if not any(j % 2 == 0 for j in str(i))])

B:
def unique_digits(x):
    return sorted([i for i in x if all(j % 2 != 0 for j in str(i))])

C:
def unique_digits(x):
    return sorted([i for i in x if not any(j % 2 != 0 for j in str(i))])

D:
def unique_digits(x):
    return sorted([i for i in x if all(j % 2 == 0 for j in str(i))])

E:
def unique_digits(x):
    return sorted([i for i in x if not any(j == 2 for j in str(i))])

F:
def unique_digits(x):
    return sorted([i for i in x if all(j == 2 for j in str(i))])

G:
def unique_digits(x):
    return sorted([i for i in x if any(j == 2 for j in str(i))])

H:
def unique_digits(x):
    return sorted([i for i in x if all(j != 2 for j in str(i))])

