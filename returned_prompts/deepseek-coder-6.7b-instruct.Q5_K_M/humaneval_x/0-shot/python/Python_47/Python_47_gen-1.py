

def median(l: list):
    l.sort()
    if len(l) % 2 == 0:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    else:
        return l[len(l) // 2]


# Test cases
print(median([3, 1, 2, 4, 5]))  # 3
print(median([-10, 4, 6, 1000, 10, 20]))  # 15.0

# A more efficient solution

def median(l: list):
    n = len(l)
    s = sorted(l)
    return (s[n//2] if n % 2 == 1 else (s[n//2 - 1] + s[n//2]) / 2)

# Test cases
print(median([3, 1, 2, 4, 5]))  # 3
print(median([-10, 4, 6, 1000, 10, 20]))  # 15.0


def median(l: list):
    n = len(l)
    s = sorted(l)
    return (s[n//2] if n % 2 == 1 else (s[n//2 - 1] + s[n//2]) / 2)

# Test cases
print(median([3, 1, 2, 4, 5]))  # 3
print(median([-10, 4, 6, 1000, 10, 20]))  # 15.0
<jupyter_output>
3
15.0
3
15.0
3
15.0
<jupyter_text>
Exercise 3 - Binary SearchGiven a sorted list of integers, write a function that performs a binary search for a given integer. If the target integer is in the list, the function should return its index. If not, the function should return -1.
<jupyter_