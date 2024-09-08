def is_lucid(n):
    digits = [int(d) for d in str(n)]
    return sum(digits) % 2 == 0 or sum(digits) % 5 == 0
def get_ludic(n):
    return [i for i in range(1, n+1) if is_lucid(i)]