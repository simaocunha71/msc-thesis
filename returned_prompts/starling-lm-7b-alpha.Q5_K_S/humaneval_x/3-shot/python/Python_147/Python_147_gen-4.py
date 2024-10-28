    def f(n):
        return (n*(n+1))//2
    def g(n):
        return n*(n+1)

    a = []
    for i in range(1, n+1):
        a.append(i*i-i+1)

    b = []
    c = []
    for elem in a:
        if elem % 3 == 0:
            b.append(elem)
        else:
            c.append(elem)

    b.sort()
    c.sort()

    result = 0
    for elem_b in b:
        left = 0
        right = len(c)-1
        while left <= right:
            mid = left + (right - left)//2
            if c[mid] + elem_b < 3:
                left = mid + 1
            elif c[mid] + elem_b == 3:
                result += 1
                left = mid + 1
            else:
                right = mid - 1

    return result


