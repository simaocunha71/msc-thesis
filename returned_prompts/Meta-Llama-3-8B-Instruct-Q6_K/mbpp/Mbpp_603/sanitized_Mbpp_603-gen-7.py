def get_ludic(n):
    return [i for i in range(1, n+1) if i % 2 == 1]  # lucid numbers are odd numbers
    # return [i for i in range(1, n+1) if i % 3 == 0]  # lucid numbers are multiple of 3
    # return [i for i in range(1, n+1) if i % 2 == 0 and i % 3 == 0]  # lucid numbers are multiple of 2 and 3
    # return [i for i in range(1, n+1) if i % 2 == 0 and i % 3 != 0]  # lucid numbers are multiple of 2 but not 3
    # return [i for i in range(1, n+1) if i % 3 == 0 and i % 2 != 0]  # lucid numbers are multiple of 3 but not 2
    # return [i for i in range(1, n+1) if i % 2 != 0 and i % 3 != 0]  # lucid numbers are not multiple of 2 and 3
    # return [i for i in range(1, n+1) if i % 2 == 0 or i % 3 == 0]  # lucid numbers are multiple of 2 or 3
    # return [i for i in range(1, n+1) if i % 2 != 0 or i % 3 != 0]  # lucid numbers are not multiple of 2 or 3
    # return [i for i in range(1, n+1) if i % 2 == 0 or i % 3 != 0]  # lucid numbers are multiple of 2 or not 3
    # return [i for i in range(1, n+1) if i % 2 != 0 or i % 3 == 0]  # lucid numbers are not 2 or multiple of 3
    # return [i for i in range(1, n+1) if i % 2 == 0 and i % 3 != 0]  # lucid numbers are multiple of 2 but not 3
    # return [i for i