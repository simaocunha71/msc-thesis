def sum_product(numbers):
    return sum(numbers),prod(numbers)

B:
def sum_product(numbers):
    if len(numbers)==0:
        return 0,1
    else:
        return sum(numbers),prod(numbers)

C:
def sum_product(numbers):
    return sum(numbers),1

D:
def sum_product(numbers):
    return 0,1

E:
def sum_product(numbers):
    return sum(numbers),sum(numbers)

F:
def sum_product(numbers):
    return 0,0

A. A
B. B
C. C
D. D
E. E
F. F