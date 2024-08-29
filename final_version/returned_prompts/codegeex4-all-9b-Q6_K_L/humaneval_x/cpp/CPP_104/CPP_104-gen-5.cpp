def unique_digits(x):
    return [i for i in sorted(x) if all(int(d) % 2 != 0 for d in str(i))]

B:
def unique_digits(x):
    return [i for i in x if all(int(d) % 2 != 0 for d in str(i))]

C:
def unique_digits(x):
    return sorted([i for i in x if all(int(d) % 2 != 0 for d in str(i))])

D:
def unique_digits(x):
    return sorted(x) if all(int(d) % 2 != 0 for d in str(x)) else []

E:
def unique_digits(x):
    return [i for i in sorted(x) if all(int(d) % 2 != 0 for d in str(i))] if x else []

F:
def unique_digits(x):
    return [i for i in x if all(int(d) % 2 != 0 for d in str(i))] if x else sorted(x)

G:
def unique_digits(x):
    return [i for i in x if all(int(d) % 2 != 0 for d in str(x))] if x else sorted(x)

H:
def unique_digits(x):
    return [i for i in sorted(x) if all(int(d) % 2 != 0 for d in str(x))] if x else []

I:
def unique_digits(x):
    return [i for i in sorted(x) if all(int(d) % 2 == 0 for d in str(i))]

J:
def unique_digits(x):
    return sorted([i for i in x if all(int(d) % 2 == 0 for d in str(i))])

K:
def unique_digits(x):
    return [i for i in x if all(int(d) % 2 == 0 for d in str(x))] if x else sorted(x)

L:
def unique_digits(x):
    return sorted([i for i in x if all(int(d) % 2 == 0 for d in str(i))]) if x else []

M:
def unique_digits(x):
    return [i for i in x if all(int(d) % 2 == 0 for d in str(x))] if x else sorted([i for i in x if all(int(d) % 2 != 0 for d in str(i))])

N:
def unique_digits(x):
    return sorted([i for i in x if all(int(d) % 2