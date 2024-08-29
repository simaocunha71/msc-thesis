def unique_digits(x):
    return [i for i in x if not any(j%2==0 for j in str(i))]

B:
def unique_digits(x):
    return [i for i in x if not any(int(j)%2==0 for j in str(i))]

C:
def unique_digits(x):
    return [i for i in x if not any(int(j)%2==0 for j in str(i).zfill(2))]

D:
def unique_digits(x):
    return [i for i in x if not any(int(j)%2==0 for j in str(i).rjust(2, '0'))]

E:
def unique_digits(x):
    return [i for i in x if not any(int(j)%2==0 for j in str(i).ljust(2, '0'))]

F:
def unique_digits(x):
    return [i for i in x if not any(int(j)%2==0 for j in str(i).zfill(1))]

G:
def unique_digits(x):
    return [i for i in x if not any(int(j)%2==0 for j in str(i).rjust(1, '0'))]

H:
def unique_digits(x):
    return [i for i in x if not any(int(j)%2==0 for j in str(i).ljust(1, '0'))]

I:
def unique_digits(x):
    return [i for i in x if not any(int(j)%2==0 for j in str(i).zfill(0))]

J:
def unique_digits(x):
    return [i for i in x if not any(int(j)%2==0 for j in str(i).rjust(0, '0'))]

K:
def unique_digits(x):
    return [i for i in x if not any(int(j)%2==0 for j in str(i).ljust(0, '0'))]

L:
def unique_digits(x):
    return [i for i in x if not any(int(j)%2==0 for j in str(i).zfill(-1))]

M:
def unique_digits(x):
    return [i for i in x if not any(int(j)%2==0 for j in str(i).rjust(-1, '0'))]

N:
def unique_digits(x):
    return [i for i in x if not any(int(j)%2==0 for j in str(i).ljust(-1, '