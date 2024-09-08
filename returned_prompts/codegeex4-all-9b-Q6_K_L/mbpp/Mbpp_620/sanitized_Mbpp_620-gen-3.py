def largest_subset(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    numbers.sort()
    subset = [numbers[0]]
    for num in numbers[1:]:
        lcm_subset = subset[-1]
        for i in range(len(subset) - 1, -1, -1):
            lcm_subset = lcm(lcm_subset, subset[i])
            if num % lcm_subset == 0:
                subset.append(num)
                break
    return len(subset)