def recursive_list_sum(l):
    flat_list = [item for sublist in l for item in sublist]
    return sum(flat_list)

def recursive_list_sum(l):
    if isinstance(l[0], list):
        return recursive_list_sum(l) + recursive_list_sum(l[0])
    else:
        return l[0] + recursive_list_sum(l[1:])


def recursive_list_sum(l):
    if len(l) > 1:
        return l[0] + recursive_list_sum(l[1:])
    elif isinstance(l[0], list):
        return recursive_list_sum(l) + recursive_list_sum(l[0])
    else:
        return l[0]

def recursive_list_sum(l):
    if len(l) > 1:
        return l[0] + recursive_list_sum(l[1:])
    elif isinstance(l[0], list):
        return recursive_list_sum(l) + recursive_list_sum(l[0])
    else:
        return l[0]


def recursive_list_sum(l):
    if len(l) > 1:
        return l[0] + recursive_list_sum(l[1:])
    elif isinstance(l[0], list):
        return recursive_list_sum(l) + recursive_list_sum(l[0])
    else:
        return l[0]

def recursive_list_sum(l):
    if len(l) > 1:
        return l[0] + recursive_list_sum(l[1:])
    elif isinstance(l[0], list):
        return recursive_list_sum(l) + recursive_list_sum(l[0])
    else:
        return l[0]

def recursive_list_sum(l):
    if len(l) > 1:
        return l[0] + recursive_list_sum(l[1:])
   