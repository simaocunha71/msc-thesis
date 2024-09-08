def eulerian_num(n, m):
    # If m is greater than n, return 0 as it is not possible to choose m elements from n elements
    if m > n:
        return 0

    # If m is 0, return 1 as there is only one way to choose 0 elements from n elements
    if m == 0:
        return 1

    # If m is equal to n, return 1 as there is only one way to choose n elements from n elements
    if m == n:
        return 1

    # If m is 1, return n as there are n ways to choose 1 element from n elements
    if m == 1:
        return n

    # If n is 1, return 1 as there is only one way to choose 1 element from 1 element
    if n == 1:
        return 1

    # If n is 2, return 2 as there are 2 ways to choose 1 element from 2 elements
    if n == 2:
        return 2

    # If n is greater than 2 and m is 2, return n as there are n ways to choose 2 elements from n elements
    if m == 2:
        return n

    # If n is greater than 2 and m is greater than 2, return (n-1) * eulerian_num(n-1, m-1) + eulerian_num(n-1, m)
    return (n-1) * eulerian_num(n-1, m-1) + eulerian_num(n-1, m)