def is_sublist(lst, sub):
    return sub in lst

print(is_sublist([2,4,3,5,7],[3,7]))

# Solution 2:
def is_sublist(lst, sub):
    len_sub = len(sub)
    return any(sub == lst[i:i+len_sub] for i in range(len(lst)))

print(is_sublist([2,4,3,5,7],[3,7]))

# Solution 3:
def is_sublist(lst, sub):
    s=set(lst)
    for i in sub:
        if i not in s:
            return False
    return True

print(is_sublist([2,4,3,5,7],[3,7]))

# Solution 4:
def is_sublist(lst, sub):
    lst_str = ''.join(map(str, lst))
    sub_str = ''.join(map(str, sub))
    return sub_str in lst_str

print(is_sublist([2,4,3,5,7],[3,7]))

# Solution 5:
def is_sublist(lst, sub):
    return all(x in lst for x in sub)

print(is_sublist([2,4,3,5,7],[3,7]))

# Solution 6:
def is_sublist(lst, sub):
    return any(lst[i:i+len(sub)] == sub for i in range(len(lst)-len(sub)+1))

print(is_sublist([2,4,3,5,7],[3,7]))

# Solution 7:
def is_sublist(lst, sub):
    return sub in ''.join(map(str, lst))

print(is_sublist([2,4,3,5,7],[3,7]))

# Solution 8:
def is_sublist(lst, sub):
    return any(all