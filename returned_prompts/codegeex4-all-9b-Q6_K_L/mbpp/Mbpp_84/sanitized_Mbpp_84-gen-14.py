def sequence(n):
    newman_conway = [1, 1]
    for i in range(2, n+1):
        if i % 2 == 0:
            newman_conway.append(newman_conway[i // 2])
        else:
            newman_conway.append(newman_conway[(i - 1) // 2] + newman_conway[(i + 1) // 2])
    return newman_conway[-1]