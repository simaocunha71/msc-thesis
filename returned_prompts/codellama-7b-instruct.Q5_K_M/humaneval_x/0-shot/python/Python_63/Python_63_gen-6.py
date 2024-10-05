

def fibfib(n: int) -> int:
    fibfib_list = [0, 0, 1]
    for i in range(3, n + 1):
        fibfib_list.append(fibfib_list[i - 1] + fibfib_list[i - 2] + fibfib_list[i - 3])
    return fibfib_list[n]

B:


def fibfib(n: int) -> int:
    fibfib_list = [0, 0, 1]
    for i in range(3, n + 1):
        fibfib_list.append(fibfib_list[i - 1] + fibfib_list[i - 2] + fibfib_list[i - 3])
    return fibfib_list[-1]

C:


def fibfib(n: int) -> int:
    fibfib_list = [0, 0, 1]
    fibfib_list.append(fibfib_list[1] + fibfib_list[2] + fibfib_list[3])
    for i in range(4, n + 1):
        fibfib_list.append(fibfib_list[i - 1] + fibfib_list[i - 2] + fibfib_list[i - 3])
    return fibfib_list[-1]

D:


def fibfib(n: int) -> int:
    if n in (0, 1):
        return n
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)

E:


def fibfib(n: int) -> int:
    if n < 4:
        return n
    else:
        return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)

F:


def fibfib(n: int) -> int:
    if n < 4