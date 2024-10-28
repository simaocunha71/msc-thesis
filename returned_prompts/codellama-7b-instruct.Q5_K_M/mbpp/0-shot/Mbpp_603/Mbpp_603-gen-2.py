"""
def get_ludic(n):
    ludic = [1]
    while ludic[-1] < n:
        ludic.append(sum(ludic[:-1]) + 1)
    return ludic
"""
