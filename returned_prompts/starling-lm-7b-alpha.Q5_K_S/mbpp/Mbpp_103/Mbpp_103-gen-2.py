def eulerian_num(n, m):
    if n < m:
        return 0
    if n == m:
        return 1
    if m == 1:
        return n + 1
    if m == 0:
        return 1
    if n == 0:
        return 0
    #if m < 0:
    #    return eulerian_num(n, -m)
    #if m > 0:
    #    return eulerian_num(n - 1, m - 1)
    #if m == 0:
    #    return eulerian_num(n - 1, 0)
    return eulerian_num(n - 1, m) + eulerian_num(n - 1, m - 1)


"""
"""
def test_eulerian_num():
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(3, 0) == 3
    assert eulerian_num(2, 1) == 2
    assert eulerian_num(2, 0) == 2
    assert eulerian_num(1, 1) == 1
    assert eulerian_num(1, 0) == 1
    assert eulerian_num(0, 1) == 0
    assert eulerian_num(0, 0) == 1
    assert eulerian_num(3, 2) == 7
    assert eulerian_num(3, 3) == 4
    assert eulerian_num(3, 4) == 0
    assert eulerian_num(3, 5) == 0
    assert eulerian_num(4, 3) == 10
    assert eulerian_num(4, 4) == 4
    assert eulerian_num(4, 5) == 0
    assert eulerian_num(4, 6) == 0
    assert eulerian_num(5, 4) == 10
    assert eulerian_num(5, 5