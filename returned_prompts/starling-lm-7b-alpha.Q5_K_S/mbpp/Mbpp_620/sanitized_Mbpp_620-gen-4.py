def largest_subset(seq):
    divisors = set()
    for i, num in enumerate(seq):
        if num % 2 == 0:
            divisors.add(2)
        for j in range(i+1, len(seq)):
            if seq[j] % num == 0:
                divisors.add(seq[j])
    return len(divisors)