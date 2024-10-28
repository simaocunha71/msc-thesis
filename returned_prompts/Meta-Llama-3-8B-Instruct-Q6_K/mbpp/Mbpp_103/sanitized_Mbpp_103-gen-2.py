def eulerian_num(n, m):
    if m > n:
        return 0
    if m == 0:
        return 1
    return eulerian_num(n-1, m-1) + (n-1)*eulerian_num(n-1, m) + eulerian_num(n-1, m)  # base case: eulerian_num(0,0)=1