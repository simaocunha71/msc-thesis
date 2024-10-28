
def fruit_distribution(s,n):
    oranges, apples = s.split('and')
    oranges, apples = int(oranges.strip(' oranges')), int(apples.strip(' apples'))
    return n - oranges - apples