def bell_number(n):
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    return bell[n][0]

assert bell_number(2)==2
assert bell_bell(3)==5
assert bell_bell(4)==15
assert bell_bell(5)==52
assert bell_bell(6)==203
assert bell_bell(7)==877
assert bell_bell(8)==4140
assert bell_bell(9)==21147
assert bell_bell(10)==115975
"""

