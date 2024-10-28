def isBored(S):
    return sum(1 for x in S.split('. ') + S.split('? ') + S.split('! ') if x.startswith("I"))