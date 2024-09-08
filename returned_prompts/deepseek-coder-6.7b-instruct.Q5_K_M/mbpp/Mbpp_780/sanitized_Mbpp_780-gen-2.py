from itertools import chain, combinations
def find_combinations(arr):
    all_combinations = []
    for i in range(len(arr) + 1):
        all_combinations += list(chain(*[combinations(arr, i) for _ in range(i)]))
    sums = [(sum(x[0] for x in combo), sum(x[1] for x in combo)) for combo in all_combinations]
    return sums