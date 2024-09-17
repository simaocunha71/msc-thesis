def sequence(n):
    newman_conway = [0, 1, 1]
    for i in range(3, n+1):
        newman_conway.append(newman_conway[newman_conway[i-1]] + newman_conway[i - newman_conway[i-1]])
    return newman_conway[n]