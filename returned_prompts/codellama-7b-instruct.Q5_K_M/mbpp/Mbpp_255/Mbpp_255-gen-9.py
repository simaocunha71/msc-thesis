def combinations_colors(colors, n):
    if n == 1:
        return [(c,) for c in colors]
    else:
        combos = []
        for c in colors:
            for p in combinations_colors(colors, n-1):
                combos.append((c,) + p)
        return combos
