"""
def combinations_colors(colors, n):
    if n == 1:
        return [(c,) for c in colors]
    else:
        combos = []
        for i, color in enumerate(colors):
            for c in combinations_colors(colors[i+1:], n-1):
                combos.append((color,) + c)
        return combos
"""
