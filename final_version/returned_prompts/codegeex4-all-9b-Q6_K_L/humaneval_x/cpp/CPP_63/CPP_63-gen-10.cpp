def fibfib(n):
    fibfib_list = [0, 0, 1]
    for i in range(3, n+1):
        fibfib_list.append(fibfib_list[i-1] + fibfib_list[i-2] + fibfib_list[i-3])
    return fibfib_list[n]

