    if len(xs) % 2 == 1 or xs[0] == 0:
        raise ValueError("xs must have even length and non zero first coefficient")

    x = xs[0]
    for i in range(1, len(xs), 2):
        x -= poly([-xs[i + 1], xs[i]], x) / poly([1, -x], x)
    return x


