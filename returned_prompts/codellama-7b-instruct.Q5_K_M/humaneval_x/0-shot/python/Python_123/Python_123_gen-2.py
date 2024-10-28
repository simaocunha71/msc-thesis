
def get_odd_collatz(n):
    if n < 1:
        return []
    sequence = [n]
    while sequence[-1] != 1:
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] // 2)
        else:
            sequence.append(3 * sequence[-1] + 1)
    return [x for x in sequence if x % 2 != 0]

