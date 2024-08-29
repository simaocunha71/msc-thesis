def count_nums(n):
    count = 0
    for i in n:
        sum = 0
        i = abs(i)
        while i > 0:
            sum += i % 10
            i = i // 10
        if sum > 0:
            count += 1
    return count

B:
def count_nums(n):
    count = 0
    for i in n:
        sum = 0
        while i > 0:
            sum += i % 10
            i = i // 10
        if sum > 0:
            count += 1
    return count

C:
def count_nums(n):
    count = 0
    for i in n:
        sum = 0
        while i > 0:
            sum += i % 10
            i = i // 10
        if sum > 0:
            count += 1
        if i < 0:
            i = abs(i)
    return count

D:
def count_nums(n):
    count = 0
    for i in n:
        sum = 0
        i = abs(i)
        while i > 0:
            sum += i % 10
            i = i // 10
        if sum > 0:
            count += 1
        if i < 0:
            i = -i
    return count

E:
def count_nums(n):
    count = 0
    for i in n:
        sum = 0
        while i > 0:
            sum += i % 10
            i = i // 10
        if sum > 0:
            count += 1
        if i < 0:
            i = -i
    return count

F:
def count_nums(n):
    count = 0
    for i in n:
        sum = 0
        while i > 0:
            sum += i % 10
            i = i // 10
        if sum > 0:
            count += 1
        if i < 0:
            i = abs(i)
            sum = -sum
    return count

G:
def count_nums(n):
    count = 0
    for i in n:
        sum = 0
        while i > 0:
            sum += i % 10
            i = i // 10
        if sum > 0