from math import sqrt
def generate_perrin_numbers(limit):
    perrin_numbers = []
    for a in range(1, int(sqrt(limit)) + 1):
        for b in range(a, int(sqrt(limit)) + 1):
            if (a * a + b * b) > limit:
                break
            if (a * a + b * b) in perrin_numbers:
                continue
            for c in range(b, int(sqrt(limit)) + 1):
                if (c * c + (a * a + b * b)) > limit:
                    break
                if (c * c + (a * a + b * b)) in perrin_numbers:
                    continue
                if (c * c + (a * a + b * b)) <= limit:
                    perrin_numbers.append(c * c + (a * a + b * b))
    return perrin_numbers
def cal_sum(limit):
    perrin_numbers = generate_perrin_numbers(limit)
    return sum(perrin_numbers)