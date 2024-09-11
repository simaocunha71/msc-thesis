def dict_depth(d):
    if isinstance(d, dict):
        return 1 + max(map(dict_depth, d.values()))
    elif isinstance(d, list):
        return 1 + max(map(dict_depth, d))
    else:
        return 0

from collections import defaultdict
def dict_depth(d):
    if isinstance(d, dict):
        return 1 + max(dict_depth(v) for v in d.values())
    elif isinstance(d, list):
        return 1 + max(dict_depth(e) for e in d)
    else:
        return 0

def dict_depth(d):
    if isinstance(d, dict):
        return 1 + max(map(dict_depth, d.values()))
    elif isinstance(d, list):
        return 1 + max(map(dict_depth, d))
    else:
        return 0

from collections import defaultdict
def dict_depth(d):
    if isinstance(d, dict):
        return 1 + max(map(dict_depth, d.values()))
    elif isinstance(d, list):
        return 1 + max(map(dict_depth, d))
    else:
        return 0


def dict_depth(d):
    if isinstance(d, dict):
        return 1 + max(map(dict_depth, d.values()))
    elif isinstance(d, list):
        return 1 + max(map(dict_depth, d))
    else:
        return 0


# Python3 program to find the depth of
# a dictionary

from collections import defaultdict

# Function to find the depth of a dictionary
def dict_depth(d):
    if isinstance(d, dict):
        return 1 + max(map(dict_depth, d.values()))
    elif isinstance(d, list):
        return 1 + max(map(dict_depth, d))
    else:
        return 0


# Driver code
if __name__ == "__main__":
    d = {'a':1, 'b': {'c': {'d': {}}}}
    print(dict