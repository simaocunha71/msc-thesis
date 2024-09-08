def fibfib(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

B:
def fibfib(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    fibfibList = [0, 0, 1]
    for i in range(3, n+1):
        fibfibList.append(fibfibList[i-1] + fibfibList[i-2] + fibfibList[i-3])
    return fibfibList[n]

C:
def fibfib(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    fibfibList = [0, 0, 1]
    while len(fibfibList) < n+1:
        fibfibList.append(fibfibList[-1] + fibfibList[-2] + fibfibList[-3])
    return fibfibList[n]

D:
def fibfib(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    fibfibList = [0, 0, 1]
    for i in range(3, n+1):
        fibfibList[i] = fibfibList[i-1] + fibfibList[i-2] + fibfibList[i-3]
    return fibfibList[n]

E:
def fibfib(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    fibfibList = [0, 0, 1]
    for i in range(3, n+1):
        fibfibList.append(fibfibList[i-1] + fibfibList[i-2] + fibfibList[i-3])
    return fibfibList[-1]
