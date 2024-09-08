def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

B:
def fibfib(n):
    fibfib_list = [0, 0, 1]
    for i in range(3, n+1):
        fibfib_list.append(fibfib_list[i-1] + fibfib_list[i-2] + fibfib_list[i-3])
    return fibfib_list[n]

C:
def fibfib(n):
    fibfib_list = [0, 0, 1]
    for i in range(3, n+1):
        fibfib_list.append(fibfib_list[i-1] + fibfib_list[i-2] + fibfib_list[i-3])
    return fibfib_list[n]

D:
def fibfib(n):
    fibfib_list = [0, 0, 1]
    for i in range(3, n+1):
        fibfib_list.append(fibfib_list[i-1] + fibfib_list[i-2] + fibfib_list[i-3])
    return fibfib_list[n]

E:
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

F:
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

G:
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

H:
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n ==