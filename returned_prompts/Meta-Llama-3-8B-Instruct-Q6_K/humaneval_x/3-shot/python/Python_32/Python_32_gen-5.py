    if len(xs) % 2 == 0 and max([abs(i) for i in xs]) != 0:
        x = -xs[1] / xs[0]
        return round(x, 2)
    else:
        return None


