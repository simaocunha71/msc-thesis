def is_squarefree(n):
    # 1 is squarefree
    if n == 1:
        return 1

    # 2 is squarefree
    if n == 2:
        return 2

    # 3 is squarefree
    if n == 3:
        return 3

    # 4 is not squarefree
    if n == 4:
        return 5

    # for n > 4
    i = 5
    count = 5
    while True:
        # flag to check if number is squarefree
        is_squarefree = True
        # check if number is divisible by any number up to its square root
        for j in range(2,