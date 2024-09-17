def eulerian_num(n, m):
    # The number of Eulerian cycles in a graph with n vertices and m edges is
    # n - k + 1, where k is the number of vertices of odd degree.
    # The sum of the degrees of all the vertices is twice the number of edges,
    # so the number of vertices of odd degree is 
    # (sum of degrees) mod 2.
    # In particular, if all the vertices have even degree, then the Eulerian number
    # is 2.

    # In this case, n is even and m is even, so all the vertices have even degree.
    if n % 2 == 0 and m % 2 == 0:
        return 2

    # Otherwise, compute the number of vertices of odd degree.
    else:
        # The number of vertices of odd degree is at most n,
        # so we can compute the sum of the degrees modulo 2 by repeatedly adding 2 to the sum
        # until the sum is at most n.
        k = 0
        while (m + k) % 2 == 0:
            k += 2
        return n - k + 1