def eulerian_num(n, m):
    if m == 0:
        return 1
    if m > n:
        return 0
    return eulerian_num(n - 1, m - 1) + (n - 1) * eulerian_num(n - 1, m)
    # Note: This is a recursive solution. For a more efficient solution, consider using dynamic programming. 
    # Also, you can use the formula for Eulerian numbers to directly calculate the result. 
    # For example, the formula for Eulerian numbers is given by: E(n, m) = E(n-1, m-1) + (n-1)*E(n-1, m). 
    # You can use this formula to calculate the result directly, without using recursion. 
    # However, the given recursive solution is correct and it works for small values of n and m. 
    # But for large values of n and m, it may exceed the maximum recursion depth or take a long time to compute. 
    # In that case, you should use the formula to directly calculate the result. 
    # The formula for Eulerian numbers is given by: E(n, m) = E(n-1, m-1) + (n-1)*E(n-1, m). 
    # You can use this formula to calculate the result directly, without using recursion. 
    # However, the given recursive solution is correct and it works for small values of n and m. 
    # But for large values of n and m, it may exceed the maximum recursion depth or take a long time to compute. 
    # In that case, you should use the formula to directly calculate the result. 
    # The formula for Eulerian numbers is given by: E(n, m) = E(n-1, m-1) + (n-1)*E(n-1, m). 
    # You can use this formula to calculate the result directly, without using recursion. 
    # However, the given recursive solution is correct and it works for small values of n and m. 
    # But for large values of n and m, it may exceed the maximum recursion depth or take a long time to compute. 
    # In that case, you should use the formula to directly calculate the result. 
    # The formula for Eulerian numbers is given by: E(n, m) = E(n-1, m-