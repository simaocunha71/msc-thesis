def eulerian_num(n, m):
    """
    Find the Eulerian number a(n, m).

    Complexity: O(n) time, O(n) space.

    :param int n: The number of vertices in the graph.
    :param int m: The number of edges in the graph.
    :return: The Eulerian number a(n, m).
    :rtype: int
    """
    # Eulerian number a(n, m) can be computed by the following recurrence relation:
    #    a(n, m) = sum(i=0..m) [C(m, i) * (n - i)^n]
    # where C(m, i) is the binomial coefficient of m choose i.
    #
    # In order to compute a(n, m) in O(n) time, we can compute the binomial coefficient
    # in O(1) time using the following identity:
    #    C(m, i) = C(m, m - i) = m! / (i! * (m - i)!)
    # and use Newton's binomial approximation to compute (n - i)^n in O(1) time.
    #
    # The total space complexity is O(n) due to the storage of the intermediate results.

    # First, we compute the binomial coefficients in O(1) time.
    #
    # Note that a(n, m) = 0 if m > 2 * n, since a graph with n vertices and m edges
    # cannot be Eulerian if m > 2 * n.
    if m > 2 * n:
        return 0
    # Compute C(m, i) for i in range(m + 1).
    # Note that C(m, m) = 1, and C(m, i) = C(m, m - i) = m! / (i! * (m - i)!)
    C = [1] * (m + 1)
    for i in range(m + 1):
        if i > 0:
            C[i] = i * C[i - 1]