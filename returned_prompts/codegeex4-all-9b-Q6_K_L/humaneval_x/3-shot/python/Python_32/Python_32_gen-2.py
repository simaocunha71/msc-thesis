    a = xs[0]
    b = xs[1]
    c = xs[2]
    d = xs[3]

    # calculate the roots
    root1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    root2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

    # return the root with the smallest absolute value
    return min(root1, root2, key=abs)


