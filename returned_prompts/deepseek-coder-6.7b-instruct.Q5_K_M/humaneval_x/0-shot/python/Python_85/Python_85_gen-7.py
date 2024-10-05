
def add(lst):
    return sum(lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0)

print(add([4, 2, 6, 7])) #==> 2



def add(lst):
    sum = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum

print(add([4, 2, 6, 7])) #==> 2



def add(lst):
    sum = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum

print(add([4, 2, 6, 7])) #==> 2



def add(lst):
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            sum += lst[i]
    return sum

print(add([4, 2, 6, 7])) #==> 2
<jupyter_output>
2
2
2
2
<jupyter_text>
