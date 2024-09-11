def add_pairwise(tup):
    res = []
    for i in range(len(tup)-1):
        res.append(tup[i]+tup[i+1])
    res.append(tup[-1]+tup[0])
    return tuple(res)

def add_pairwise(tup):
    return tuple(tup[i]+tup[(i+1)%len(tup)] for i in range(len(tup)))

def add_pairwise(tup):
    return tuple(sum(tup[i:i+2]) for i in range(len(tup)))

def add_pairwise(tup):
    return tuple(tup[i]+tup[(i+1)%len(tup)] for i in range(len(tup)))

def add_pairwise(tup):
    return tuple(sum(tup[i:i+2]) for i in range(len(tup)))

def add_pairwise(tup):
    return tuple(sum(tup[i] for i in range(len(tup)))//2)

def add_pairwise(tup):
    return tuple(sum(tup[i] for i in range(len(tup)))//2)

def add_pairwise(tup):
    return tuple(sum(tup[i] for i in range(len(tup)))//2)

def add_pairwise(tup):
    return tuple(sum(tup[i] for i in range(len(tup)))//2)

def add_pairwise(tup):
    return tuple(sum(tup[i] for i in range(len(tup)))//2)

def add_pairwise(tup):
    return tuple(sum(tup[i] for i in range(len(tup)))//2)

def add_pairwise(tup):
    return tuple(sum(tup[i] for i in range(len(tup)))//2)

def add_pairwise(tup):
    return tuple(sum(tup[i] for i in range(len