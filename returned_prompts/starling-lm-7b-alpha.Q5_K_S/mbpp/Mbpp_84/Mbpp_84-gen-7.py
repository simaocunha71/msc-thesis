def sequence(n):
    a = [0, 1]
    while len(a) < n + 1:
        a.append(a[-1] + a[-2])
    return a[n]

# assert sequence(10) == 6

def sequence_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return sequence_recursive(n-1) + sequence_recursive(n-2)

# assert sequence_recursive(10) == 6

def sequence_generator(n):
    a = [0, 1]
    while len(a) < n + 1:
        a.append(a[-1] + a[-2])
    return a[n]

# assert sequence_generator(10) == 6

def sequence_generator_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return sequence_generator_recursive(n-1) + sequence_generator_recursive(n-2)

# assert sequence_generator_recursive(10) == 6

def sequence_generator_recursive_memoize(n):
    memo = {0: 0, 1: 1}
    def memoized(i):
        if i not in memo:
            memo[i] = memoized(i-1) + memoized(i-2)
        return memo[i]
    return memoized(n)

# assert sequence_generator_recursive_memoize(10) == 6

def sequence_generator_recursive_memoize_generator(n):
    memo = {0: 0, 1: 1}
    def memoized(i):
        if i not in memo:
            memo[i] = yield from memoized(i-1) + yield from memoized(i-2)
        yield memo[i]
    return memoized(n)

# assert sequence_generator_recursive_