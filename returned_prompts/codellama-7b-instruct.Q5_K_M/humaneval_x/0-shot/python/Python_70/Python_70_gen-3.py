
def strange_sort_list(lst):
    return sorted(lst, key=lambda x: x, reverse=True)

# OR

def strange_sort_list(lst):
    return sorted(lst, key=lambda x: -x)

# OR

def strange_sort_list(lst):
    return sorted(lst, key=lambda x: x)

# OR

def strange_sort_list(lst):
    return sorted(lst, key=lambda x: -x, reverse=True)



