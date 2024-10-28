```
def simplify(x, n):
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    common = max(x_den, n_den)
    while common != 1:
        if x_den % common == 0 and n_den % common == 0:
            x_num //= common
            x_den //= common
            n_num //= common
            n_den //= common
        common -= 1
    return x_num * n_num == x_den * n_den
```