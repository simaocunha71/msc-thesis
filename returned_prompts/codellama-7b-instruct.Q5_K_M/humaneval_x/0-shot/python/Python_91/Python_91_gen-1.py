
def is_bored(S):
    return sum(1 for c in S.split('.') if c.startswith("I"))
