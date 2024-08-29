def larg_nnum(lst, n):
    lst.sort(reverse=True)
    return lst[:n]

print(set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2)))

# Output: {100, 90}

