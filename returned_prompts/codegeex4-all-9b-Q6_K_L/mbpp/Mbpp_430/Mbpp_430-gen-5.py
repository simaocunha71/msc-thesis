def parabola_directrix(a, h, k):
    """
    Calculates the directrix of a parabola given its equation in the form ax^2 + bx + c = 0
    and the coordinates of its vertex (h, k).
    """
    a = float(a)
    h = float(h)
    k = float(k)
    if a == 0:
        raise ValueError("a cannot be zero")
    if a < 0:
        a = -a
        k = -k
    directrix = (4 * a * h + (1 - 4 * a * k)) / (4 * a)
    return directrix

