def sum_list(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

assert sum_list([10,20,30],[15,25,35])==[25,45,65]
"""

