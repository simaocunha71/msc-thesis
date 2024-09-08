def largest_subset(numbers):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def lcm(x, y):
        return x * y // gcd(x, y)

    def pair_lcm(a, b):
        return lcm(a, b) // gcd(a, b)

    numbers.sort()
    subsets = [[num] for num in numbers]
    max_size = 1

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[j] % numbers[i] == 0:
                for subset in subsets:
                    if subset and numbers[i] % pair_lcm(subset[-1], numbers[j]) == 0:
                        subset.append(numbers[j])
                        max_size = max(max_size, len(subset))

    return max_size