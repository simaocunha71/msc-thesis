def unique_digits(x):
    return sorted([i for i in x if len([j for j in str(i) if int(j)%2==0])==0])
B:
def unique_digits(x):
    return sorted([i for i in x if not any(int(d) % 2 == 0 for d in str(i))])
C:
def unique_digits(x):
    return sorted([i for i in x if sum([1 for j in str(i) if int(j)%2==0])==0])
D:
def unique_digits(x):
    return sorted([i for i in x if sum([1 for j in str(i) if int(j)==2 or int(j)==4 or int(j)==6 or int(j)==8])==0])

E:
def unique_digits(x):
    return sorted([i for i in x if sum([1 for j in str(i) if int(j) in {2, 4, 6, 8}])==0])

F:
def unique_digits(x):
    return sorted([i for i in x if not any(int(d) % 2 == 0 for d in str(i))])
G:
def unique_digits(x):
    return sorted([i for i in x if sum([1 for j in str(i) if int(j)%2==0])==0])
H:
def unique_digits(x):
    return sorted([i for i in x if not any(int(d) % 2 == 0 for d in str(i))])

I:
def unique_digits(x):
    return sorted([i for i in x if len([j for j in str(i) if int(j)%2==0])==0])
J:
def unique_digits(x):
    return sorted([i for i in x if any(int(d) % 2 == 0 for d in str(i))])
K:
def unique_digits(x):
    return sorted([i for i in x if sum([1 for j in str(i) if int(j) in {2, 4, 6, 8}])==0])

L:
def unique_digits(x):
    return sorted([i for i in x if sum([1 for j in str(i) if int(j)==2 or int(j)==4 or int(j)==6 or int(j)==8])==0])

M:
def unique_digits(x):
    return sorted([i for i in x if not any(int(d) % 2 == 0 for d in str(i))])
N:
def unique_digits(x