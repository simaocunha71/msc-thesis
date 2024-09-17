def combinations_colors(colors,n):
    if len(colors) < n:
        return []
    if n==0:
        return [()]
    if n==1:
        return [(c,) for c in colors]
    else:
        return [(colors[i],)+comb for i,comb in enumerate(combinations_colors(colors[1:],n-1))]